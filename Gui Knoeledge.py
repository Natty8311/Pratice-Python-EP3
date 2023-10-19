from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox



GUI = Tk() #นี้คือหน้าจอหลักของโปรเเกรม
GUI.title('โปรเเกรมบันทึกข้อมูล') #นี่คือชื่อโปรเเกรม
GUI.geometry('500x400')#นี่คือขนาดของโปรเเกรม



B1 = ttk.Button(GUI,text='เงินมีอยู่เท่าไร')
B1.pack(ipadx=20,ipady=20)

FB1 = Frame(GUI)
FB1.place(x=100,y=300)

def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู๋300bath'
    messagebox.showinfo('เงินในบัญชี',text)

B2 = ttk.Button(FB1,text='เงินมีอยู่เท่าไร',command=Button2)
B2.pack(ipadx=20,ipady=20)


GUI.mainloop()
