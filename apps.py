from tkinter import *
root = Tk()
root.title("Perhitungan")
root.geometry("420x400")
root.config(background="white")

#judul
l1=Label(text="Pilih yang ingin dicari", bg="lightyellow", font="normal 30")
l1.grid(row=0, column=0, columnspan=5, pady=20, padx=30)

pilihan =0

#fungsi
def Tegangan():
   global pilihan
   pilihan = 1
   l2.config(text="Arus")
   l3.config(text="Hambatan")
   l4.config(text="X")
   l5.config(text="Hasil Tegangan")
   l6.config(text="")

def Arus():
   global pilihan
   pilihan = 2
   l2.config(text="Tegangan")
   l3.config(text="Hambatan")
   l4.config(text="/")
   l5.config(text="Hasil Arus")
   l6.config(text="")

def Hambatan():
   global pilihan
   pilihan = 3
   l2.config(text="Tegangan")
   l3.config(text="Arus")
   l4.config(text="/")
   l5.config(text="Hasil Hambatan")
   l6.config(text="")

def total():
    global pilihan
    if pilihan==1:
        rumus=int(e1.get())*int(e2.get())
        l6.config(text=rumus)

    if pilihan==2:
        rumus=int(e1.get())/int(e2.get())
        l6.config(text=rumus)  

    if pilihan==3:
        rumus=int(e1.get())/int(e2.get())
        l6.config(text=rumus)  


#button
b1=Button(text="Tegangan", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=10,command=Tegangan)
b1.grid(row=1,column=0)

b2=Button(text="Arus", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=10,command=Arus)
b2.grid(row=1,column=1)

b3=Button(text="Hambatan", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=10,command=Hambatan)
b3.grid(row=1,column=2)

#label penanda
l2=Label(text="",bg="lightyellow",font="normal 20")
l2.grid(row=2,column=0,pady=(40,0))

l3=Label(text="",bg="lightyellow",font="normal 20")
l3.grid(row=2,column=2,pady=(40,0))

#input dan tombol
e1=Entry(bd=5, relief=RIDGE, font="normal 20", width=10)
e1.grid(row=3,column=0)

l4=Label(text="",font="normal 20",bg="lightyellow")
l4.grid(row=3,column=1)

e2=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e2.grid(row=3,column=2)

b4=Button(text="Hitung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=10,command=total)
b4.grid(row=3,column=3)

#hasil
l5=Label(text="",font="normal 20",bg="lightyellow")
l5.grid(row=4,column=0,columnspan=4,pady=30)

l6=Label(text="",font="normal 20",bg="lightyellow")
l6.grid(row=5,column=0,columnspan=4,pady=10)

root.mainloop()