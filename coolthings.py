from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
 
root = Tk()
root.title("Stay Up To Date")
root.geometry("500x350")
titleheight = 5
def test(event):
 print(event) #ensure that this line is indented
topframe = Frame(root,bg='#50d987',height='20')
topframe.pack(fill=X) # make as wide as root
title = Label(topframe,text="Your Y9 Schedules!",fg="white",bg='#50d987')
title.config(font=("Arial", 18))
title.pack(ipady=titleheight/2)
can1 = Canvas(topframe,height='20',bg="#50d987",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.pack(side=LEFT, padx=8, pady=1)



spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)
frame = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.pack(fill=None, expand=False)
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)
b1=Button(frame, text="Day 1")
b2=Button(frame, text="Day 2")
b3=Button(frame, text="Day 3")
b4=Button(frame, text="Day 4")
b5=Button(frame, text="Day 5")
b6=Button(frame, text="Day 6")
b7=Button(frame, text="Day 7")
b8=Button(frame, text="Day 8")


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=3)
b4.grid(row=0, column=4)
b5.grid(row=0, column=5)
b6.grid(row=0, column=6)
b7.grid(row=0, column=7)
b8.grid(row=0, column=8)

root.mainloop()







