from tkinter import *
root = Tk()
root.title("Menghitung Keliling dan Luas Bangun Datar hehe")
root.geometry("730x480")
root.config(background="white")

#judul
l1=Label(text="Pilih Bangun Datar", bg="lightyellow", font="normal 30")
l1.grid(row=0, column=0, columnspan=5, pady=15, padx=25)
pilihan = 0

#fungsi
def Persegi():
   global pilihan
   pilihan = 1
   l2.config(text="Sisi")
   l3.config(text="")
   l4.config(text="")
   l9.config(text="")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Persegi_Panjang():
   global pilihan
   pilihan = 2
   l2.config(text="Panjang")
   l3.config(text="Lebar")
   l4.config(text="")
   l9.config(text="")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Segitiga():
   global pilihan
   pilihan = 3
   l2.config(text="a")
   l3.config(text="b")
   l4.config(text="c")
   l9.config(text="")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Lingkaran():
   global pilihan
   pilihan = 4
   l2.config(text="Jari-jari")
   l3.config(text="")
   l4.config(text="")
   l9.config(text="")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Trapesium():
   global pilihan
   pilihan = 5
   l2.config(text="a")
   l3.config(text="b")
   l4.config(text="c")
   l9.config(text="d")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Jajar_Genjang():
   global pilihan
   pilihan = 6
   l2.config(text="Alas")
   l3.config(text="Tinggi")
   l4.config(text="")
   l9.config(text="")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Belah_Ketupat():
   global pilihan
   pilihan = 7
   l2.config(text="Diagonal 1")
   l3.config(text="Diagonal 2")
   l4.config(text="Sisi")
   l9.config(text="Sisi")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def Layang_layang():
   global pilihan
   pilihan = 8
   l2.config(text="Diagonal 1")
   l3.config(text="Diagonal 2")
   l4.config(text="Sisi")
   l9.config(text="Sisi")
   l5.config(text="Keliling")
   l6.config(text="")
   l7.config(text="Luas")
   l8.config(text="")

def total():
    global pilihan
    if pilihan==1:
        Keliling_persegi=4*int(e1.get())
        l6.config(text=Keliling_persegi)
        Luas_persegi=int(e1.get())*int(e1.get())
        l8.config(text=Luas_persegi)

    if pilihan==2:
        Keliling_persegi_panjang=2*(int(e1.get())+int(e2.get()))
        l6.config(text=Keliling_persegi_panjang)
        Luas_persegi_panjang=int(e1.get())*int(e2.get())
        l8.config(text=Luas_persegi_panjang) 

    if pilihan==3:
        Keliling_segitiga=int(e1.get())+int(e2.get())+int(e3.get())
        l6.config(text=Keliling_segitiga)
        Luas_segitiga=1/2*int(e1.get())*int(e2.get())
        l8.config(text=Luas_segitiga) 
     
    if pilihan==4:
        Keliling_lingkaran=2*22/7*int(e1.get())
        l6.config(text=Keliling_lingkaran)
        Luas_lingkaran=22/7*int(e1.get())*int(e1.get())
        l8.config(text=Luas_lingkaran) 

    if pilihan==5:
        Keliling_trapesium=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())
        l6.config(text=Keliling_trapesium)
        Luas_trapesium=1/2*int(e1.get())*int(e2.get())+int(e3.get())
        l8.config(text=Luas_trapesium)

    if pilihan==6:
        Keliling_jajar_genjang=2*(int(e1.get())+int(e2.get()))
        l6.config(text=Keliling_jajar_genjang)
        Luas_jajar_genjang=int(e1.get())*int(e2.get())
        l8.config(text=Luas_jajar_genjang) 

    if pilihan==7:
        Keliling_belah_ketupat=4*int(e3.get())
        l6.config(text=Keliling_belah_ketupat)
        Luas_belah_ketupat=1/2*int(e1.get())*int(e2.get())
        l8.config(text=Luas_belah_ketupat) 
     
    if pilihan==8:
        Keliling_layang_layang=2*(int(e3.get())+int(e4.get()))
        l6.config(text=Keliling_layang_layang)
        rumus_layang_layang=1/2*int(e1.get())*int(e2.get())
        l8.config(text=rumus_layang_layang) 

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

#button
b1=Button(text="Persegi", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Persegi)
b1.grid(row=1,column=0)

b2=Button(text="Persegi Panjang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Persegi_Panjang)
b2.grid(row=1,column=1)

b3=Button(text="Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Segitiga)
b3.grid(row=1,column=2)

b4=Button(text="Lingkaran", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Lingkaran)
b4.grid(row=1,column=3)

b5=Button(text="Trapesium", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Trapesium)
b5.grid(row=2,column=0)

b6=Button(text="Jajar Genjang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Jajar_Genjang)
b6.grid(row=2,column=1)

b7=Button(text="Belah Ketupat", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Belah_Ketupat)
b7.grid(row=2,column=2)

b8=Button(text="Layang-layang", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Layang_layang)
b8.grid(row=2,column=3)

#label penanda
l2=Label(text="",bg="lightyellow",font="normal 20")
l2.grid(row=3,column=0,pady=(40,0))

l3=Label(text="",bg="lightyellow",font="normal 20")
l3.grid(row=3,column=1,pady=(40,0))

l4=Label(text="",bg="lightyellow",font="normal 20")
l4.grid(row=3,column=2,pady=(40,0))

l9=Label(text="",bg="lightyellow",font="normal 20")
l9.grid(row=3,column=3,pady=(40,0))

#input dan tombol
e1=Entry(bd=5, relief=RIDGE, font="normal 20", width=10)
e1.grid(row=4,column=0)

e2=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e2.grid(row=4,column=1)

e3=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e3.grid(row=4,column=2)

e4=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e4.grid(row=4,column=3)

b9=Button(text="Hitung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=total)
b9.grid(row=5,column=3)

#hasil
l5=Label(text="",font="normal 20",bg="lightyellow")
l5.grid(row=5,column=0,columnspan=2,pady=30)

l6=Label(text="",font="normal 20",bg="lightyellow")
l6.grid(row=6,column=0,columnspan=2,pady=10)

l7=Label(text="",font="normal 20",bg="lightyellow")
l7.grid(row=5,column=0,columnspan=4,pady=30)

l8=Label(text="",font="normal 20",bg="lightyellow")
l8.grid(row=6,column=0,columnspan=4,pady=10)

root.mainloop()