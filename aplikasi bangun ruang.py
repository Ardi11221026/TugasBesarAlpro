from tkinter import *
root = Tk()
root.title("Menghitung Luas Permukaan dan Volume Bangun Ruang")
root.geometry("730x480")
root.config(background="white")

#judul
l1=Label(text="Pilih Bangun Ruang", bg="lightyellow", font="normal 30")
l1.grid(row=0, column=0, columnspan=5, pady=15, padx=25)
pilihan = 0

#fungsi
def Kubus():
   global pilihan
   pilihan = 1
   l2.config(text="Sisi")
   l3.config(text="")
   l4.config(text="")
   l5.config(text="Luas Permukaan")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Balok():
   global pilihan
   pilihan = 2
   l2.config(text="Panjang")
   l3.config(text="Lebar")
   l4.config(text="Tinggi")
   l5.config(text="Luas Permukaan")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Prisma_Segitiga():
   global pilihan
   pilihan = 3
   l2.config(text="Alas")
   l3.config(text="Tinggi")
   l4.config(text="Tinggi Prisma")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Limas_Segiempat():
   global pilihan
   pilihan = 4
   l2.config(text="Panjang")
   l3.config(text="Lebar")
   l4.config(text="Tinggi")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Limas_Segitiga():
   global pilihan
   pilihan = 5
   l2.config(text="Alas")
   l3.config(text="Tinggi")
   l4.config(text="Tinggi Limas")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Tabung():
   global pilihan
   pilihan = 6
   l2.config(text="Jari-jari")
   l3.config(text="Tinggi Tabung")
   l4.config(text="")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Kerucut():
   global pilihan
   pilihan = 7
   l2.config(text="Jari-jari")
   l3.config(text="Tinggi")
   l4.config(text="Selimut")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def Bola():
   global pilihan
   pilihan = 8
   l2.config(text="Jari-jari")
   l3.config(text="")
   l4.config(text="")
   l5.config(text="Luas")
   l6.config(text="")
   l7.config(text="Volume")
   l8.config(text="")

def total():
    global pilihan
    if pilihan==1:
        Luas_permukaan_kubus=6*int(e1.get())*int(e1.get())
        l6.config(text=Luas_permukaan_kubus)
        Volume_kubus=int(e1.get())*int(e1.get())*int(e1.get())
        l8.config(text=Volume_kubus)

    if pilihan==2:
        Luas_permukaan_balok=2*((int(e1.get())*int(e2.get()))+(int(e1.get())*int(e3.get()))+(int(e2.get())*int(e3.get())))
        l6.config(text=Luas_permukaan_balok)
        Volume_balok=int(e1.get())*int(e2.get())*int(e3.get())
        l8.config(text=Volume_balok) 

    if pilihan==3:
        Luas_permukaan_prisma_segitiga=(2*int(e1.get())*int(e2.get())/2)+(int(e1.get())+int(e2.get())*int(e3.get()))
        l6.config(text=Luas_permukaan_prisma_segitiga)
        Volume_prisma_segitiga=1/2*int(e1.get())*int(e2.get())*int(e3.get())
        l8.config(text=Volume_prisma_segitiga) 
     
    if pilihan==4:
        Luas_permukaan_limas_segiempat=(int(e1.get())*int(e2.get()))+(4*1/2*int(e1.get())*int(e2.get())*int(e3.get()))
        l6.config(text=Luas_permukaan_limas_segiempat)
        Volume_limas_segiempat=1/3*int(e1.get())*int(e2.get())*int(e3.get())
        l8.config(text=Volume_limas_segiempat) 

    if pilihan==5:
        Luas_permukaan_limas_segitiga=(1/3)+(3*1/2*int(e1.get())*int(e2.get())*int(e3.get()))
        l6.config(text=Luas_permukaan_limas_segitiga)
        Volume_limas_segitiga=1/3*(1/2*int(e1.get())*int(e2.get()))*(int(e3.get()))
        l8.config(text=Volume_limas_segitiga)

    if pilihan==6:
        Luas_permukaan_tabung=2*22/7*int(e1.get())*(int(e1.get())+int(e2.get()))
        l6.config(text=Luas_permukaan_tabung)
        Volume_tabung=22/7*int(e1.get())*int(e1.get())*int(e2.get())
        l8.config(text=Volume_tabung) 

    if pilihan==7:
        Luas_permukaan_kerucut=22/7*int(e1.get())*(int(e1.get())+int(e3.get()))
        l6.config(text=Luas_permukaan_kerucut)
        Volume_kerucut=1/3*22/7*int(e1.get())*int(e1.get())*int(e2.get())
        l8.config(text=Volume_kerucut) 
     
    if pilihan==8:
        Luas_permukaan_bola=4*22/7*int(e1.get())*int(e1.get())
        l6.config(text=Luas_permukaan_bola)
        Volume_bola=4/3*22/7*int(e1.get())*int(e1.get())*int(e1.get())
        l8.config(text=Volume_bola) 

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

#button
b1=Button(text="Kubus", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Kubus)
b1.grid(row=1,column=0)

b2=Button(text="Balok", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Balok)
b2.grid(row=1,column=1)

b3=Button(text="Prisma Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Prisma_Segitiga)
b3.grid(row=1,column=2)

b4=Button(text="Limas Segi Empat", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Limas_Segiempat)
b4.grid(row=1,column=3)

b5=Button(text="Limas Segitiga", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Limas_Segitiga)
b5.grid(row=2,column=0)

b6=Button(text="Tabung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Tabung)
b6.grid(row=2,column=1)

b7=Button(text="Kerucut", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Kerucut)
b7.grid(row=2,column=2)

b8=Button(text="Bola", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=Bola)
b8.grid(row=2,column=3)

#label penanda
l2=Label(text="",bg="lightyellow",font="normal 20")
l2.grid(row=3,column=0,pady=(40,0))

l3=Label(text="",bg="lightyellow",font="normal 20")
l3.grid(row=3,column=1,pady=(40,0))

l4=Label(text="",bg="lightyellow",font="normal 20")
l4.grid(row=3,column=2,pady=(40,0))

#input dan tombol
e1=Entry(bd=5, relief=RIDGE, font="normal 20", width=10)
e1.grid(row=4,column=0)

e2=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e2.grid(row=4,column=1)

e3=Entry(bd=5,relief=RIDGE,font="normal 20",width=10)
e3.grid(row=4,column=2)

b9=Button(text="Hitung", activebackground="lightblue",bd=5,relief=RIDGE,font="normal 15",width=15,command=total)
b9.grid(row=4,column=3)

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