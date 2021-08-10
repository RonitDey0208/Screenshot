from tkinter import *

import time
from PIL import ImageTk,Image
import sqlite3

conn = sqlite3.connect('my_db.db')
c = conn.cursor()


root = Tk()
root.geometry('600x650')
root.title('UpTime')
# root.configure(background='#edb06b')


label = Label(text="")
label = Label(text="CLIENT SOFTWARE",bg = "#022a5d",fg = "white",width="300", height="1", font=("Calibri 36 bold")).pack()

Label(text="").pack()

def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        
        return "%02d:%02d:%02d" % (hour, minutes, seconds)
        

def loadImage():
    
    filename = ImageTk.PhotoImage(resize_image)
    canvas.image = filename
    canvas.create_image(0,0,anchor='nw',image=filename)
    
    return


global count 
count = -1
run = False
def var_name(mark):
    
    def value():
      if run:
         global count
         # Just beore starting
         if count == -1:
            show = "Connecting..."
         else:
            show = str(convert(count))
         mark['text'] = show
         #Increment the count after
         #every 1 second
         mark.after(1000, value)
         count += 1
    value()
# While Running
def Start(mark):
    msg7 = Label(text="5 mins ago..",fg = "blue",width="30", height="1",font=("Calibri 13"))
    msg7.pack()
    msg1 = Label(text="CONNECTION ESTABLISHED SUCCESSFULLY!!",fg = "#022a5d",width="40", height="1",font=("Calibri 18 bold"))
    msg1.pack()
   
    stmt = """SELECT * FROM login_details """
    c.execute(stmt)
    data1 = c.fetchone()
    conn.commit()
    msg6 = Label(text=f"Client name:{data1[0]}",fg = "blue",width="30", height="1",font=("Calibri 13"))
    msg6.pack(side=RIGHT,anchor=W,padx=1,pady=5)
    global run
    run = True
    var_name(mark)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    loadImage()
    
     
# While stopped
def Stop():
   global run
   global count 
   start['state'] = 'normal'
   stop['state'] = 'disabled'
  
   run = False

   
   c.execute(f"INSERT INTO duration(session) VALUES ({count});")

   conn.commit()
   count = -1
   if run == False:
      
      mark['text'] = 'Click to reconnect'
   else:
      mark['text'] = 'Start'


mark = Label(root, text="Connect to Server", fg="brown",font="Times 25 bold")
mark.pack()
msg2 = Label(text= "")
msg2.pack()
start = Button(root, text='Connect',width=25, command=lambda: Start(mark))
stop = Button(root, text='Stop', width=25, state='disabled', command=Stop)


# img.pack()
start.pack()
stop.pack()
msg2 = Label(text= "")
msg2.pack()

msg2 = Label(text="Working duration:",fg = "#022a5d",width="30", height="1",font=("Times 20 bold"))
msg2.pack()
tot_time = 0
st = c.execute("SELECT session FROM duration;")
for sec in st:
   tot_time = tot_time + sec[0]
   con_tt = convert(tot_time)
msg3 = Label(text=(con_tt),fg = "green",width="30", height="1",font=("Calibri 16 bold"))
msg3.pack()
conn.commit()


img = Image.open("ss.png")
resize_image = img.resize((300, 300))
canvas = Canvas(root, width = 250, height = 250)
canvas.pack()

root.mainloop()
conn.close()