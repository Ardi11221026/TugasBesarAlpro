from cProfile import label
from tkinter import *
root = Tk()
root.title("Perhitungan Bangun Datar")
root.geometry("410x380")
root.config(background="white")

#judul
l1=Label(text="Pilih Bangun Datar", bg="lightyellow", font="normal 30",)
l1.grid(row=0, column=0, columnspan=5, pady=20, padx=30)
pilihan =0

#jendela baru masing-masing 
def Persegi():
    newwindow = Toplevel(root)
    newwindow.title("Persegi")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()
    
def Persegi_Panjang():
    newwindow = Toplevel(root)
    newwindow.title("Persegi Panjang")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Jajar_Genjang():
    newwindow = Toplevel(root)
    newwindow.title("Jajar Genjang")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Segitiga():
    newwindow = Toplevel(root)
    newwindow.title("Segitiga")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Belah_Ketupat():
    newwindow = Toplevel(root)
    newwindow.title("Belah Ketupat")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Layang_layang():
    newwindow = Toplevel(root)
    newwindow.title("Layang-layang")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Trapesium():
    newwindow = Toplevel(root)
    newwindow.title("Trapesium")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Lingkaran():
    newwindow = Toplevel(root)
    newwindow.title("Lingkaran")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

#button
b1=Button(text="Persegi", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Persegi)
b1.grid(row=1,column=2)

b2=Button(text="Persegi Panjang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Persegi_Panjang)
b2.grid(row=2,column=2)

b3=Button(text="Jajar Genjang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Jajar_Genjang)
b3.grid(row=3,column=2)

b4=Button(text="Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Segitiga)
b4.grid(row=4,column=2)

b5=Button(text="Belah Ketupat", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Belah_Ketupat)
b5.grid(row=1,column=3)

b6=Button(text="Layang-layang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Layang_layang)
b6.grid(row=2,column=3)

b7=Button(text="Trapesium", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Trapesium)
b7.grid(row=3,column=3)

b8=Button(text="Lingkaran", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Lingkaran)
b8.grid(row=4,column=3)

root.mainloop()