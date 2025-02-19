from ast import Break

print("Program menghitung Luas Permukaan dan Volume") 
def menu():
   print("Pilih Bangun Ruang") 
   print("1. Kubus") 
   print("2. Balok") 
   print("3. Prisma Segitiga")
   print("4. Limas Segi Empat")
   print("5. Limas Segitiga")
   print("6. Tabung")
   print("7. Kerucut")
   print("8. Bola")
   
def Kubus():
   print("Menghitung Luas Permukaan dan Volume")
   s =int(input("Masukkan Panjang sisi : "))
   luas_permukaan=6*s*s
   volume=s*s*s
   print(f"Luas Permukaan Kubus adalah {luas_permukaan}, dan Volume Kubus adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

def Balok():
   print("Menghitung Luas Permukaan dan Volume")
   p = int(input("Masukkan Panjang : "))
   l = int(input("Masukkan Lebar : "))
   t = int(input("Masukkan Tinggi : "))
   luas_permukaan=2*(p*l)+(p*t)+(l*t)
   volume=p*l*t
   print(f"Luas Permukaan Balok adalah {luas_permukaan}, dan Volume Balok adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()
 
def Prisma_Segitiga():
   print("Menghitung Luas Permukaan dan Volume")
   a = int(input("Masukkan Alas : "))
   t = int(input("Masukkan Tinggi : "))
   T = int(input("Masukkan Tinggi Prisma : "))
   luas_permukaan=(2*(a*t)/2)+(a+a+a*T)
   volume=(a*t)/2*T
   print(f"Luas Permukaan Prisma Segitiga adalah {luas_permukaan}, dan Volume Prisma Segitiga adalah {volume}")
   print
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()
 
def Limas_Segi_Empat():
   print("Menghitung Luas Permukaan dan Volume")
   p = int(input("Masukkan Panjang : "))
   l = int(input("Masukkan Lebar : "))
   t = int(input("Masukkan Tinggi : "))
   luas_permukaan=(p*l)+(4*1/2*p*l*t)
   volume=1/3*p*l*t
   print(f"Luas Permukaan Limas Segi Empat adalah {luas_permukaan}, dan Volume Limas Segi Empat adalah {volume}")
   print
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

def Limas_Segitiga():
   print("Menghitung Luas Permukaan dan Volume")
   a = int(input("Masukkan Alas : "))
   t = int(input("Masukkan Tinggi : "))
   T = int(input("Masukkan Tinggi Limas : "))
   luas_permukaan=(1/3)+(3*1/2*a*t*T)
   volume=1/3*(1/2*a*t)*T
   print(f"Luas Permukaan Limas Segitiga {luas_permukaan}, dan Volume Limas Segitiga adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

def Tabung():
   print("Menghitung Luas Permukaan dan Volume")
   r = int(input("Masukkan jari-jari : "))
   t = int(input("Masukkan Tinggi : "))
   phi = 22/7
   luas_permukaan=2*phi*r*(r+t)
   volume=phi*r*r*t
   print(f"Luas Permukaan Tabung adalah {luas_permukaan}, dan Volume Tabung adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

def Kerucut():
   print("Menghitung Luas Permukaan dan Volume ")
   r = int(input("Masukkan jari-jari : "))
   t = int(input("Masukkan Tinggi : "))
   s = int(input("Masukkan Garis Pelukis Kerucut : "))
   phi = 22/7
   luas_permukaan=phi*r*(r+s)
   volume=1/3*phi*r*r*t
   print(f"Luas Permukaan Kerucut adalah {luas_permukaan}, dan Volume Kerucut adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

def Bola():
   print("Menghitung Luas Permukaan dan Volume")
   r = int(input("Masukkan jari-jari : "))
   phi = 22/7
   luas_permukaan=4*phi*r*r
   volume=4/3*phi*r*r*r
   print(f"Luas Permukaan Bola adalah {luas_permukaan}, dan Volume Bola adalah {volume}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya" or "ya":
      menu()
   else:
      exit()

menu()
while 1 :
   pilih=int(input("Masukkan Pilihan : "))
   if pilih==1:
      Kubus()
   elif pilih==2:
      Balok()
   elif pilih==3:
      Prisma_Segitiga()
   elif pilih==4:
      Limas_Segi_Empat()
   elif pilih==5:
      Limas_Segitiga() 
   elif pilih==6:
      Tabung()
   elif pilih==7:
      Kerucut()
   elif pilih==8:
      Bola()
      print("Terimakasih telah mencoba")
      break
   else :
      print("Maaf, pilihan yang anda masukkan tidak tersedia")
      print("Silahkan coba kembali")
      coba=input().upper()
      if coba=="Ya/Tidak":
         menu()
      else:
         exit()
         break