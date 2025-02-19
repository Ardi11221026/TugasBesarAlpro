from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Kalkulator Bangun Datar")
window.setGeometry(400, 50, 500, 400)

lbl_window = QLabel("Silahkan Pilih Bangun Datar")
lbl_window.setFixedSize(400, 50)
lbl_window.setFont(QFont("Arial", 24))

def buat_tombol(label):
    btn = QPushButton(label, window)
    btn.setFont(QFont("Arial", 11))
    btn.setFixedSize(200, 50)
    return btn

btn_Persegi = buat_tombol("Persegi")
btn_PersegiPanjang = buat_tombol("Persegi Panjang")
btn_Segitiga = buat_tombol("Segitiga")
btn_Lingkaran = buat_tombol("Lingkaran")
btn_Trapesium = buat_tombol("Trapesium")
btn_JajarGenjang = buat_tombol("Jajar Genjang")
btn_BelahKetupat = buat_tombol("Belah Ketupat")
btn_LayangLayang = buat_tombol("Layang-layang")

def buat_layout(layout):
    lyt = QHBoxLayout()
    lyt.addWidget(layout)
    return lyt

layout_hor1 = buat_layout(lbl_window)
layout_hor2 = buat_layout(btn_Persegi)
layout_hor2.addWidget(btn_PersegiPanjang)
layout_hor3 = buat_layout(btn_Segitiga)
layout_hor3.addWidget(btn_Lingkaran)
layout_hor4 = buat_layout(btn_Trapesium)
layout_hor4.addWidget(btn_JajarGenjang)
layout_hor5 = buat_layout(btn_BelahKetupat)
layout_hor5.addWidget(btn_LayangLayang)

layout_ver = QVBoxLayout()
layout_ver.addLayout(layout_hor1)
layout_ver.addLayout(layout_hor2)
layout_ver.addLayout(layout_hor3)
layout_ver.addLayout(layout_hor4)
layout_ver.addLayout(layout_hor5)

widget = QWidget()
widget.setLayout(layout_ver)
window.setCentralWidget(widget)

def Persegi():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 400)
    windbar.setWindowTitle("Persegi")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    sisi = QLabel("Sisi", windbar)
    sisi.setFont(QFont("Arial", 13))
    sisi.move(30, 70)
    edit_sisi = QLineEdit(windbar)
    edit_sisi.setFont(QFont("Arial", 13))
    edit_sisi.setFixedSize(200, 40)
    edit_sisi.move(100, 65)
    satuan = QLabel("meter", windbar)
    satuan.setFont(QFont("Arial", 13))
    satuan.move(310, 70)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 120)

    def total():
        try:
            s = float(edit_sisi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = 4*s
            L = s*s

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 220)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 270)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 330)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def PersegiPanjang():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 450)
    windbar.setWindowTitle("Persegi Panjang")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    panjang = QLabel("Panjang", windbar)
    panjang.setFont(QFont("Arial", 13))
    panjang.move(30, 70)
    edit_panjang = QLineEdit(windbar)
    edit_panjang.setFont(QFont("Arial", 13))
    edit_panjang.setFixedSize(200, 40)
    edit_panjang.move(110, 65)
    satuan_panjang = QLabel("meter", windbar)
    satuan_panjang.setFont(QFont("Arial", 13))
    satuan_panjang.move(320, 70)

    lebar = QLabel("Lebar", windbar)
    lebar.setFont(QFont("Arial", 13))
    lebar.move(30, 130)
    edit_lebar = QLineEdit(windbar)
    edit_lebar.setFont(QFont("Arial", 13))
    edit_lebar.setFixedSize(200, 40)
    edit_lebar.move(110, 125)
    satuan_lebar = QLabel("meter", windbar)
    satuan_lebar.setFont(QFont("Arial", 13))
    satuan_lebar.move(320, 130)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 180)

    def total():
        try:
            p = float(edit_panjang.text())
            l = float(edit_lebar.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = 2*(p+l) 
            L = p*l

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 230)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 280)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 330)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 390)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def Segitiga():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 550)
    windbar.setWindowTitle("Segitiga")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    alas = QLabel("Alas", windbar)
    alas.setFont(QFont("Arial", 13))
    alas.setFixedWidth(400)
    alas.move(30, 70)
    edit_alas = QLineEdit(windbar)
    edit_alas.setFont(QFont("Arial", 13))
    edit_alas.setFixedSize(200, 40)
    edit_alas.move(160, 65)
    satuan_alas = QLabel("meter", windbar)
    satuan_alas.setFont(QFont("Arial", 13))
    satuan_alas.move(370, 70)

    tinggi = QLabel("Tinggi", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 130)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 125)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 130)

    miring = QLabel("Miring", windbar)
    miring.setFont(QFont("Arial", 13))
    miring.setFixedWidth(400)
    miring.move(30, 190)
    edit_miring = QLineEdit(windbar)
    edit_miring.setFont(QFont("Arial", 13))
    edit_miring.setFixedSize(200, 40)
    edit_miring.move(160, 185)
    satuan_miring = QLabel("meter", windbar)
    satuan_miring.setFont(QFont("Arial", 13))
    satuan_miring.move(370, 190)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 240)

    def total():
        try:
            a = float(edit_alas.text())
            t = float(edit_tinggi.text())
            m = float(edit_miring.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = a+t+m
            L = ((a * t) / 2)

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 310)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 360)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 420)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 470)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def Lingkaran():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 400)
    windbar.setWindowTitle("Lingkaran")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    jarijari = QLabel("Jari-jari", windbar)
    jarijari.setFont(QFont("Arial", 13))
    jarijari.setFixedWidth(400)
    jarijari.move(30, 70)
    edit_jarijari = QLineEdit(windbar)
    edit_jarijari.setFont(QFont("Arial", 13))
    edit_jarijari.setFixedSize(200, 40)
    edit_jarijari.move(100, 65)
    satuan_jarijari = QLabel("meter", windbar)
    satuan_jarijari.setFont(QFont("Arial", 13))
    satuan_jarijari.move(310, 70)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 120)

    def total():
        try:
            r = float(edit_jarijari.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = 2*22/7*r
            L = 22/7*r*r

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 220)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 270)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 330)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def Trapesium():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 600)
    windbar.setWindowTitle("Trapesium")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    a = QLabel("a (alas)", windbar)
    a.setFont(QFont("Arial", 13))
    a.setFixedWidth(400)
    a.move(30, 70)
    edit_a = QLineEdit(windbar)
    edit_a.setFont(QFont("Arial", 13))
    edit_a.setFixedSize(200, 40)
    edit_a.move(160, 65)
    satuan_a = QLabel("meter", windbar)
    satuan_a.setFont(QFont("Arial", 13))
    satuan_a.move(370, 70)

    b = QLabel("b", windbar)
    b.setFont(QFont("Arial", 13))
    b.setFixedWidth(400)
    b.move(30, 130)
    edit_b = QLineEdit(windbar)
    edit_b.setFont(QFont("Arial", 13))
    edit_b.setFixedSize(200, 40)
    edit_b.move(160, 125)
    satuan_b = QLabel("meter", windbar)
    satuan_b.setFont(QFont("Arial", 13))
    satuan_b.move(370, 130)

    c = QLabel("c", windbar)
    c.setFont(QFont("Arial", 13))
    c.setFixedWidth(400)
    c.move(30, 190)
    edit_c = QLineEdit(windbar)
    edit_c.setFont(QFont("Arial", 13))
    edit_c.setFixedSize(200, 40)
    edit_c.move(160, 185)
    satuan_c = QLabel("meter", windbar)
    satuan_c.setFont(QFont("Arial", 13))
    satuan_c.move(370, 190)

    d = QLabel("d (tinggi)", windbar)
    d.setFont(QFont("Arial", 13))
    d.setFixedWidth(400)
    d.move(30, 250)
    edit_d = QLineEdit(windbar)
    edit_d.setFont(QFont("Arial", 13))
    edit_d.setFixedSize(200, 40)
    edit_d.move(160, 245)
    satuan_d = QLabel("meter", windbar)
    satuan_d.setFont(QFont("Arial", 13))
    satuan_d.move(370, 250)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 300)

    def total():
        try:
            a = float(edit_a.text())
            b = float(edit_b.text())
            c = float(edit_c.text())
            d = float(edit_d.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:

            K = a+b+c+d
            L = 1/2 * a * d

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 410)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 470)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 530)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def JajarGenjang():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 440)
    windbar.setWindowTitle("Jajar Genjang")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    alas = QLabel("Alas", windbar)
    alas.setFont(QFont("Arial", 13))
    alas.setFixedWidth(400)
    alas.move(30, 70)
    edit_alas = QLineEdit(windbar)
    edit_alas.setFont(QFont("Arial", 13))
    edit_alas.setFixedSize(200, 40)
    edit_alas.move(160, 65)
    satuan_alas = QLabel("meter", windbar)
    satuan_alas.setFont(QFont("Arial", 13))
    satuan_alas.move(370, 70)

    tinggi = QLabel("Tinggi", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 130)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 125)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 130)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 180)

    def total():
        try:
            a = float(edit_alas.text())
            t = float(edit_tinggi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = 2*(a+t)
            L = a*t

            keliling.setText(f"Keliling              : {K:.3f} m")
            luas.setText(f"Luas                 : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 230)

    keliling = QLabel("Keliling              :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 280)

    luas = QLabel("Luas                 :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 330)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 380)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def BelahKetupat():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 500)
    windbar.setWindowTitle("Belah Ketupat")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    d1 = QLabel("Diagonal 1", windbar)
    d1.setFont(QFont("Arial", 13))
    d1.setFixedWidth(400)
    d1.move(30, 70)
    edit_d1 = QLineEdit(windbar)
    edit_d1.setFont(QFont("Arial", 13))
    edit_d1.setFixedSize(200, 40)
    edit_d1.move(160, 65)
    satuan_d1 = QLabel("meter", windbar)
    satuan_d1.setFont(QFont("Arial", 13))
    satuan_d1.move(370, 70)

    d2 = QLabel("Diagonal 2", windbar)
    d2.setFont(QFont("Arial", 13))
    d2.setFixedWidth(400)
    d2.move(30, 130)
    edit_d2 = QLineEdit(windbar)
    edit_d2.setFont(QFont("Arial", 13))
    edit_d2.setFixedSize(200, 40)
    edit_d2.move(160, 125)
    satuan_d2 = QLabel("meter", windbar)
    satuan_d2.setFont(QFont("Arial", 13))
    satuan_d2.move(370, 130)

    sisi = QLabel("Sisi", windbar)
    sisi.setFont(QFont("Arial", 13))
    sisi.setFixedWidth(400)
    sisi.move(30, 190)
    edit_sisi = QLineEdit(windbar)
    edit_sisi.setFont(QFont("Arial", 13))
    edit_sisi.setFixedSize(200, 40)
    edit_sisi.move(160, 185)
    satuan_sisi = QLabel("meter", windbar)
    satuan_sisi.setFont(QFont("Arial", 13))
    satuan_sisi.move(370, 190)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 240)

    def total():
        try:
            d1 = float(edit_d1.text())
            d2 = float(edit_d2.text())
            s = float(edit_sisi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = 4*s
            L = 1/2*d1*d2

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 290)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 340)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 390)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 450)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

def LayangLayang():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 600)
    windbar.setWindowTitle("Layang-layang")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    d1 = QLabel("Diagonal 1", windbar)
    d1.setFont(QFont("Arial", 13))
    d1.setFixedWidth(400)
    d1.move(30, 70)
    edit_d1 = QLineEdit(windbar)
    edit_d1.setFont(QFont("Arial", 13))
    edit_d1.setFixedSize(200, 40)
    edit_d1.move(160, 65)
    satuan_d1= QLabel("meter", windbar)
    satuan_d1.setFont(QFont("Arial", 13))
    satuan_d1.move(370, 70)

    d2 = QLabel("Diagonal 2", windbar)
    d2.setFont(QFont("Arial", 13))
    d2.setFixedWidth(400)
    d2.move(30, 130)
    edit_d2 = QLineEdit(windbar)
    edit_d2.setFont(QFont("Arial", 13))
    edit_d2.setFixedSize(200, 40)
    edit_d2.move(160, 125)
    satuan_d2 = QLabel("meter", windbar)
    satuan_d2.setFont(QFont("Arial", 13))
    satuan_d2.move(370, 130)

    ab = QLabel("Sisi a+b", windbar)
    ab.setFont(QFont("Arial", 13))
    ab.setFixedWidth(400)
    ab.move(30, 190)
    edit_ab = QLineEdit(windbar)
    edit_ab.setFont(QFont("Arial", 13))
    edit_ab.setFixedSize(200, 40)
    edit_ab.move(160, 185)
    satuan_ab = QLabel("meter", windbar)
    satuan_ab.setFont(QFont("Arial", 13))
    satuan_ab.move(370, 190)

    cd = QLabel("Sisi c+d", windbar)
    cd.setFont(QFont("Arial", 13))
    cd.setFixedWidth(400)
    cd.move(30, 250)
    edit_cd = QLineEdit(windbar)
    edit_cd.setFont(QFont("Arial", 13))
    edit_cd.setFixedSize(200, 40)
    edit_cd.move(160, 245)
    satuan_cd = QLabel("meter", windbar)
    satuan_cd.setFont(QFont("Arial", 13))
    satuan_cd.move(370, 250)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 300)

    def total():
        try:
            d1 = float(edit_d1.text())
            d2 = float(edit_d2.text())
            ab = float(edit_ab.text())
            cd = float(edit_cd.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            K = ab + cd
            L = 1/2*d1*d2

            keliling.setText(f"Keliling               : {K:.3f} m")
            luas.setText(f"Luas                  : {L:.3f} m^2")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 410)

    luas = QLabel("Luas                  :", windbar)
    luas.setFont(QFont("Arial", 13))
    luas.setFixedWidth(400)
    luas.move(30, 470)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 530)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

btn_Persegi.clicked.connect(Persegi)
btn_PersegiPanjang.clicked.connect(PersegiPanjang)
btn_Segitiga.clicked.connect(Segitiga)
btn_Lingkaran.clicked.connect(Lingkaran)
btn_Trapesium.clicked.connect(Trapesium)
btn_JajarGenjang.clicked.connect(JajarGenjang)
btn_BelahKetupat.clicked.connect(BelahKetupat)
btn_LayangLayang.clicked.connect(LayangLayang)

window.show()
app.exec()
