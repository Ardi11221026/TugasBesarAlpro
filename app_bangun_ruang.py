from importlib.metadata import entry_points
from tkinter import *
root = Tk()
root.title("Perhitungan Bangun Ruang")
root.geometry("410x380")
root.config(background="white")

#judul
lbl1=Label(text="Pilih Bangun Ruang", bg="white", font="normal 30",)
lbl1.grid(row=0, column=0, columnspan=5, pady=20, padx=30)

#jendela baru masing-masing 
def Kubus():
    global pilihan
    pilihan = 1
    newwindow = Toplevel()
    newwindow.title("Kubus")
    newwindow.geometry("420x400")
    lbl2=Label(newwindow,text="Panjang Sisi",font="normal 20",bg="white")
    lbl2.grid()
    entry1=Entry(newwindow,bd=5, relief=RIDGE, font="normal 20", width=10)
    entry1.grid(row=1,column=0)
    button1=Button(newwindow,text="Hitung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=10,command=Hasil_Kubus)
    button1.grid(row=1,column=3)
    lbl3=Label(newwindow,text="Hasil",font="normal 20",bg="lightyellow")
    lbl3.grid(row=4,column=0,)

def Balok():
    newwindow = Toplevel()
    newwindow.title("Balok")
    newwindow.geometry("420x400")
    lbl2= Label(newwindow,text="masih kosong")
    lbl2.grid()

def Prisma_Segitiga():
    newwindow = Toplevel()
    newwindow.title("Prisma Segitiga")
    newwindow.geometry("420x400")
    lbl2= Label(newwindow,text="masih kosong")
    lbl2.grid()

def Limas_Segi_Empat():
    newwindow = Toplevel()
    newwindow.title("Limas Segiempat")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Limas_Segitiga():
    newwindow = Toplevel()
    newwindow.title("Limas Segitiga")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Tabung():
    newwindow = Toplevel()
    newwindow.title("Tabung")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Kerucut():
    newwindow = Toplevel()
    newwindow.title("Kerucut")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Bola():
    newwindow = Toplevel()
    newwindow.title("Bola")
    newwindow.geometry("420x400")
    lbl= Label(newwindow,text="masih kosong")
    lbl.grid()

def Hasil_Kubus():
    rumus=Entry
    lbl_hasil=f"{rumus}"
    lbl_hasil.grid()
  
#button
b1=Button(text="Kubus", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Kubus)
b1.grid(row=1,column=2)

b2=Button(text="Balok", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Balok)
b2.grid(row=2,column=2)

b3=Button(text="Prisma Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Prisma_Segitiga)
b3.grid(row=3,column=2)

b4=Button(text="Limas Segi Empat", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Limas_Segi_Empat)
b4.grid(row=4,column=2)

b5=Button(text="Limas Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Limas_Segitiga)
b5.grid(row=1,column=3)

b6=Button(text="Tabung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Tabung)
b6.grid(row=2,column=3)

b7=Button(text="Kerucut", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Kerucut)
b7.grid(row=3,column=3)

b8=Button(text="Bola", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Bola)
b8.grid(row=4,column=3)

root.mainloop()