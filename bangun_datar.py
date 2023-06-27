from ast import Break

print("Program menghitung luas dan keliling") 
def menu():
   print("Pilih Menu") 
   print("1. Persegi") 
   print("2. Persegi Panjang") 
   print("3. Segitiga")
   print("4. Keluar")

def Persegi():
   print("Menghitung luas dan keliling Persegi")
   s =int(input("Masukkan Panjang sisi :"))
   luas=s*s
   keliling=4*s
   print(f"Luas Persegi adalah {luas}, dan Keliling dari Persegi adalah {keliling}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya":
      menu()
   else:
      exit()

def PersegiPanjang():
   print("Menghitung luas dan keliling Persegi Panjang")
   p = int(input("Masukkan Panjang :"))
   l = int(input("Masukkan Lebar :"))
   luas=p*l 
   keliling=2*(p+l)
   print(f"Luas Persegi Panjang adalah {luas}, dan Keliling dari Persegi Panjang adalah {keliling}")
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya":
      menu()
   else:
      exit()
 
def Segitiga():
   print("Menghitung luas Persegi Panjang")
   a = int(input("Masukkan Alas :"))
   t = int(input("Masukkan Tinggi :"))
   luas=(a*t)/2
   keliling=a+a+a
   print(f"Luas Segitiga adalah {luas}, dan Keliling dari Persegi Panjang adalah {keliling}")
   print
   print("Ingin mencoba kembali?")
   print("Ya/Tidak")
   back=input().upper()
   if back =="Ya":
      menu()
   else:
      exit()
 
menu()
while 1 :
   pilih=int(input("Masukkan Pilihan :"))
   if pilih==1:
      Persegi()
   elif pilih==2:
      PersegiPanjang()
   elif pilih==3:
      Segitiga()
   elif pilih==4:
      print("Terimakasih telah mencoba")
      break
   else :
      print("Maaf, pilihan yang anda masukkan tidak tersedia")
      print("Silahkan coba kembali")
      coba=input().upper()
      if coba=="Ya/Tidak":
         menu()
      else:
         print("Terimakasih")
         break