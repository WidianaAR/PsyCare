from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import mysql.connector
from subprocess import Popen
import os

StyleSheet = '''
QPushButton#BlueButton {
    background-color: #87CEFA;
    border-radius: 8px;
    font-size: 14px;}
QPushButton#BlueButton:hover {
    background-color: #01C9C2;
    color: #fff;}
QPushButton#BlueButton:pressed {
    background-color: #84C1BF;}
QComboBox#Menu {
    background-color: #87CEFA;
    font-size: 12px;
    font-style: italic;
    border-radius: 8px;}
QComboBox#Menu:hover {
    background-color: #01C9C2;
    color: white;}
#Font {
    font-size: 12px;}
#Font {
    font-size: 14px;}
#Kolom {
    border: 1px solid black;
    border-radius: 8px;}
'''

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="psycare",
  autocommit = True
)
cursor = db.cursor()

class Jadwal_Praktik():
    def __init__(self, nama_dokter):
        self.nama_dokter = nama_dokter
    def List_Jadwal(self):
        sql = "SELECT hari, jam_awal, jam_akhir FROM jadwal_praktik WHERE nama_dokter='{}'".format(self.nama_dokter)
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil

class Jadwal_Konsul:
    def __init__(self, nama_dokter=None, nama_pasien=None):
        self.nama_dokter = nama_dokter
        self.nama_pasien = nama_pasien
    def List_Jadwal_Dokter(self):
        sql = "SELECT pasien, tanggal, keterangan FROM jadwal_konsul WHERE dokter='{}'".format(self.nama_dokter)
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil
    def List_Jadwal_Pasien(self):
        sql = "SELECT dokter, tanggal, keterangan FROM jadwal_konsul WHERE pasien='{}'".format(self.nama_pasien)
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil

class Info:
    def __init__(self, nama):
        self.nama = nama
    def Hapus_Info(self, judul):
        sql = "DELETE FROM info WHERE judul='{}'".format(judul)
        cursor.execute(sql)

class Konsultasi:
    def __init__(self, nama_dokter=None, nama_pasien=None):
        self.nama_dokter = nama_dokter
        self.nama_pasien = nama_pasien
    def live_chat(self):
        if self.nama_dokter != "":
            os.system('start cmd /k "py server.py -port=2222"')
        else:
            os.system('start cmd /k "py client.py -port=2222"')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(300, 400)
        MainWindow.setWindowTitle("PsyCare")

        logo = QPixmap('logo.png')
        self.logo2 = QLabel()
        self.logo2.setFixedSize(285, 150)
        self.logo2.setPixmap(logo)

        self.label = QLabel('Username : ', objectName="Font")
        self.username = QTextEdit(objectName='Kolom')
        self.username.setFixedSize(181, 31)

        self.label2 = QLabel('Password : ', objectName="Font")
        self.password = QTextEdit(objectName='Kolom')
        self.password.setFixedSize(181, 31)

        self.login = QPushButton(objectName="BlueButton")
        self.login.setText('Login')
        self.login.clicked.connect(self.masuk)
        self.login.setFixedSize(QSize(121, 31))
        
        self.pilihan = QComboBox(objectName='Menu')
        self.pilihan.setMinimumSize(0,30)
        self.pilihan.addItem('.:: Pilih Status ::.')
        self.pilihan.addItem('Dokter')
        self.pilihan.addItem('Pasien')
        self.pilihan.addItem('Admin')

        self.tombol = QPushButton(objectName="BlueButton")
        self.tombol.setFixedSize(218, 30)
        self.tombol.setText('Info')
        self.tombol.clicked.connect(self.info)

        self.tombol2 = QPushButton(objectName="BlueButton")
        self.tombol2.setFixedSize(218, 30)
        self.tombol2.setText('Jadwal Praktik')
        self.tombol2.clicked.connect(self.jadwal_praktik)

        self.tombol3 = QPushButton(objectName="BlueButton")
        self.tombol3.setFixedSize(218, 30)
        self.tombol3.setText('Jadwal Konsul')

        self.tombol4 = QPushButton(objectName="BlueButton")
        self.tombol4.setFixedSize(218, 30)
        self.tombol4.setText('Konsultasi')
        self.tombol4.clicked.connect(self.konsul)

        self.tombol5 = QPushButton(objectName="BlueButton")
        self.tombol5.setFixedSize(218, 30)
        self.tombol5.setText('Logout')
        self.tombol5.clicked.connect(self.logout)

        self.tombol_tambah = QPushButton('Tambah', objectName="BlueButton")
        self.tombol_tambah.clicked.connect(self.tambah_info)
        self.tombol_hapus = QPushButton('Hapus', objectName="BlueButton")
        self.tombol_hapus.clicked.connect(self.hapus_info)

        self.label3 = QPlainTextEdit(objectName="Font")
        self.label3.setStyleSheet("border: 1px solid black;")
        self.label3.setFixedSize(1090, 505)
        self.label3.setReadOnly(True)

        self.artikel = QComboBox(objectName="Menu")
        self.artikel.setFixedSize(440, 25)

        self.nama_dokter = '' #untuk menyimmpan data login
        self.nama_pasien = ''
        self.nama_admin = ''

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.label)
        self.horizontal.addWidget(self.username)

        self.horizontal2 = QHBoxLayout()
        self.horizontal2.addWidget(self.label2)
        self.horizontal2.addWidget(self.password)
        self.horizontal3 = QHBoxLayout()

        self.vertikal = QVBoxLayout()
        self.vertikal.setAlignment(Qt.AlignVCenter)
        self.vertikal.setSpacing(30)
        self.vertikal.addWidget(self.logo2)
        self.vertikal.addLayout(self.horizontal)
        self.vertikal.addLayout(self.horizontal2)
        self.vertikal.addWidget(self.pilihan)
        self.vertikal.addWidget(self.login)

        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        MainWindow.setCentralWidget(self.widget)

    def masuk(self):
        cek = self.pilihan.currentText()
        self.user = self.username.toPlainText()
        passw = self.password.toPlainText()
        if (cek == 'Dokter'):
            sql = "SELECT * FROM dokter WHERE username='{}' AND password='{}'".format(self.user,passw)
            cursor.execute(sql)
            hasil = cursor.fetchall()
            if len(hasil) != 0:
                MainWindow.setGeometry(150, 80, 1090, 600)
                MainWindow.setWindowTitle("PsyCare - Dokter")
                self.logo2.close(), self.pilihan.close(), self.login.close(), self.label.close(), self.label2.close(), self.username.close(), self.password.close()
                self.dokter()
            else:
                self.alert()
        elif (cek=='Pasien'):
            sql = "SELECT * FROM pasien WHERE username='{}' AND password='{}'".format(self.user, passw)
            cursor.execute(sql)
            hasil = cursor.fetchall()
            if len(hasil) != 0:
                MainWindow.setGeometry(150, 80, 1090, 600)
                MainWindow.setWindowTitle("PsyCare - Pasien")
                self.logo2.close(),self.pilihan.close(),self.login.close(),self.label.close(),self.label2.close(),self.username.close(),self.password.close()
                self.pasien()
            else:
                self.alert()
        else:
            sql = "SELECT * FROM admin WHERE username='{}' AND password='{}'".format(self.user, passw)
            cursor.execute(sql)
            hasil = cursor.fetchall()
            if len(hasil) != 0:
                MainWindow.setGeometry(500, 130, 500, 120)
                MainWindow.setWindowTitle("PsyCare - Admin")
                self.logo2.close(), self.pilihan.close(), self.login.close(), self.label.close(), self.label2.close(), self.username.close(), self.password.close()
                self.admin()
            else:
                self.alert()

    def dokter(self):
        self.horizontal.setSpacing(3)
        self.horizontal.addWidget(self.tombol)
        self.horizontal.addWidget(self.tombol2)
        self.horizontal.addWidget(self.tombol3)
        self.horizontal.addWidget(self.tombol4)
        self.horizontal.addWidget(self.tombol5)
        self.vertikal.setSpacing(5)
        self.tombol3.clicked.connect(self.jadwal_konsul_dokter)
        sql = "SELECT nama FROM dokter WHERE username='{}'".format(self.user)
        cursor.execute(sql)
        hasil = [item[0] for item in cursor.fetchall()]
        self.nama_dokter = str(hasil[0])
        return self.nama_dokter

    def admin(self):
        self.horizontal.setSpacing(68)
        self.tombol.setFixedSize(150,50), self.horizontal.addWidget(self.tombol)
        self.tombol3.setFixedSize(150,50), self.tombol3.setText('User') , self.horizontal.addWidget(self.tombol3)
        self.tombol3.clicked.connect(self.admin2)
        self.tombol5.setFixedSize(150,50), self.horizontal.addWidget(self.tombol5)
        self.vertikal.setSpacing(5)
        sql = "SELECT nama FROM admin WHERE username='{}'".format(self.user)
        cursor.execute(sql)
        hasil = [item[0] for item in cursor.fetchall()]
        self.nama_admin = str(hasil[0])
        return self.nama_admin

    def admin2(self):
        Popen("python Admin.py")

    def tambah_info(self):
        Popen("python Info.py")

    def hapus_info(self):
        cek = self.artikel.currentText()
        info = Info(self.nama_admin)
        info.Hapus_Info(cek)

    def pasien(self):
        self.horizontal.setSpacing(68)
        self.horizontal.addWidget(self.tombol)
        self.horizontal.addWidget(self.tombol3)
        self.horizontal.addWidget(self.tombol4)
        self.horizontal.addWidget(self.tombol5)
        self.vertikal.setSpacing(5)
        self.tombol3.clicked.connect(self.jadwal_konsul_pasien)
        sql = "SELECT nama FROM pasien WHERE username='{}'".format(self.user)
        cursor.execute(sql)
        hasil = [item[0] for item in cursor.fetchall()]
        self.nama_pasien = str(hasil[0])
        return self.nama_pasien

    def jadwal_praktik(self):
        self.artikel.clear()
        self.label3.clear()
        self.artikel.addItem('.::Pilih Menu::.')
        self.artikel.addItem('List Jadwal')
        self.artikel.addItem('Tambah atau Hapus')
        index = self.vertikal.count()
        if index < 7:
            self.vertikal.addWidget(self.artikel)
        else:
            self.vertikal.replaceWidget(self.artikel, self.artikel)
        self.artikel.activated.connect(self.jadwal_praktik2)
        self.data = Jadwal_Praktik(self.nama_dokter)

    def jadwal_praktik2(self):
        cek = self.artikel.currentText()
        if cek == "Tambah atau Hapus" :
            Popen('python Form_JadPraktik.py')
        elif cek == "List Jadwal":
            self.label3.clear()
            self.vertikal.addWidget(self.label3)
            self.label3.appendPlainText("Format Penulisan : (Hari, Jam Awal, Jam Akhir)")
            self.label3.appendPlainText("")
            data = self.data.List_Jadwal()
            for i in data:
                self.label3.appendPlainText(str(i))

    def info(self):
        self.artikel.clear()
        self.label3.clear()
        self.artikel.addItem('.::Pilih Info::.')
        sql = "SELECT judul FROM info"
        cursor.execute(sql)
        hasil = [item[0] for item in cursor.fetchall()]
        for i in hasil:
            self.artikel.addItem(i)
        index = self.vertikal.count()
        if index < 7:
            self.vertikal.addWidget(self.artikel)
        else:
            self.vertikal.replaceWidget(self.artikel, self.artikel)
        self.artikel.activated.connect(self.info2)

    def info2(self):
        MainWindow.setGeometry(150, 80, 1090, 600)
        cek = self.artikel.currentText()
        sql = "SELECT isi_info FROM info WHERE judul='{}'".format(cek)
        cursor.execute(sql)
        hasil = cursor.fetchall()
        self.label3.clear()
        for i in hasil:
            for x in range(len(hasil)):
                self.label3.insertPlainText(i[x])
        self.vertikal.addLayout(self.horizontal3)
        self.vertikal.addWidget(self.label3)
        cek3 = self.pilihan.currentText()
        if cek3 == "Admin":
            self.horizontal3.addWidget(self.tombol_tambah), self.horizontal3.addWidget(self.tombol_hapus)

    def jadwal_konsul_dokter(self):
        self.artikel.clear()
        self.label3.clear()
        self.artikel.addItem('.::Pilih Menu::.')
        self.artikel.addItem('List Jadwal')
        self.artikel.addItem('Tambah atau Hapus')
        index = self.vertikal.count()
        if index < 7:
            self.vertikal.addWidget(self.artikel)
        else:
            self.vertikal.replaceWidget(self.artikel, self.artikel)
        self.artikel.activated.connect(self.jadwal_konsul_dokter2)
        self.data2 = Jadwal_Konsul(self.nama_dokter)

    def jadwal_konsul_dokter2(self):
        cek = self.artikel.currentText()
        if cek == "Tambah atau Hapus":
            Popen('python Form_JadKonsul.py')
        elif cek == "List Jadwal":
            self.label3.clear()
            self.vertikal.addWidget(self.label3)
            self.label3.appendPlainText("Format Penulisan : (Nama Pasien, Tanggal, Keterangan)")
            self.label3.appendPlainText("")
            data = self.data2.List_Jadwal_Dokter()
            for i in data :
                self.label3.appendPlainText(str(i))

    def jadwal_konsul_pasien(self):
        self.artikel.clear()
        self.label3.clear()
        self.artikel.addItem('.::Pilih Menu::.')
        self.artikel.addItem('List Jadwal')
        self.artikel.addItem('List Dokter')
        self.artikel.addItem('Tambah atau Hapus')
        index = self.vertikal.count()
        if index < 7:
            self.vertikal.addWidget(self.artikel)
        else:
            self.vertikal.replaceWidget(self.artikel, self.artikel)
        self.artikel.activated.connect(self.jadwal_konsul_pasien2)
        self.data2 = Jadwal_Konsul('',self.nama_pasien)

    def jadwal_konsul_pasien2(self):
        cek = self.artikel.currentText()
        if cek == "Tambah atau Hapus":
            Popen('python Form_JadKonsul.py')
        elif cek == "List Jadwal":
            self.label3.clear()
            self.vertikal.addWidget(self.label3)
            self.label3.appendPlainText("Format Penulisan : (Nama Dokter, Tanggal, Keterangan)")
            self.label3.appendPlainText("")
            data = self.data2.List_Jadwal_Pasien()
            for i in data:
                self.label3.appendPlainText(str(i))
        elif cek == "List Dokter":
            self.label3.clear()
            self.vertikal.addWidget(self.label3)
            self.label3.appendPlainText("Format Penulisan : (Nama Dokter, Email, No.Telpon, SIP, Spesialisasi, Jenis Kelamin)")
            self.label3.appendPlainText("")
            sql = "SELECT nama, email, no_telp, no_sip, gelar, spesialisasi, jenis_kelamin FROM dokter"
            cursor.execute(sql)
            results = cursor.fetchall()
            for i in results:
                self.label3.appendPlainText(str(i))

    def konsul(self):
        chat = Konsultasi(self.nama_dokter, self.nama_pasien)
        chat.live_chat()

    def alert(self):
        pesan = QMessageBox()
        pesan.setWindowTitle("Perhatian !!"), pesan.setText('Password salah atau username belum terdaftar')
        pesan.exec_()

    def logout(self):
        MainWindow.close()

db.commit()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())