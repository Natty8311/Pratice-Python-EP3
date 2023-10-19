from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


GUI = Tk()
GUI.title('โปรเเกรมหาพื้นที่ของสามเหลี่ยม')
GUI.geometry('500x400')


H1 = Label(GUI,text='โปรเเกรมคำนวณหาพื้นที่สามเหลี่ยม',font=('Angsana New',30),fg='red')
H1.place(x=45,y=0)

T1 = Label(GUI,text='ความสูง',font=('Angsana New',20),fg='black')
T1.place(x=20,y=100)

T2 = Label(GUI,text='พื้นที่ฐาน',font=('Angsana New',20),fg='black')
T2.place(x=20,y=150)

entry1 = tk.Entry(GUI,bg='green',fg='black')
entry1.place(x=150,y=115)

entry2 = tk.Entry(GUI,bg='green',fg='black')
entry2.place(x=150,y=165)

T3 = Label(GUI,text='ผลการคำนวณ',font=('Angsana New',20),fg='black')
T3.place(x=20,y=200)

entry3 = tk.Entry(GUI,bg='green',fg='black')
entry3.place(x=150,y=215)

def triagle():
    value1 = entry1.get()
    value2 = entry2.get()

    if value1.isnumeric()and value2.isnumeric():
        height = int(value1)
        base = int(value2)
        area = 0.5*base*height
        entry3.delete(0,tk.END)
        entry3.insert(0,str(area))
    else:
        messagebox.showerror('Error','Please enter valid numetric values for height and base.')
button = Button(GUI,text='คำนวณ',command=triagle)
button.place(x=180,y=250)
    
GUI.mainloop
