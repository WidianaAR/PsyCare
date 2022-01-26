from PyQt5.QtWidgets import *
import sys
import mysql.connector

StyleSheet = '''
QPushButton {
    background-color: #87CEFA;
    border-radius: 8px;
    font-size: 14px;}
QPushButton:hover {
    background-color: #01C9C2;
    color: #fff;}
QPushButton:pressed {
    background-color: #84C1BF;}
QComboBox#Menu {
    background-color: #87CEFA;
    font-size: 12px;
    font-style: italic;
    border-radius: 8px;}
QComboBox#Menu:hover {
    background-color: #01C9C2;
    color: white;}
QLabel {
    font-size: 12px;}
QTextEdit {
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

class Person:
    def __init__(self,username=None,password=None,nama=None,email=None,no_telp=None):
        self.username = username
        self.password = password
        self.nama = nama
        self.email = email
        self.no_telp = no_telp

class Dokter(Person):
    def Tambah_Dokter(self,username,password,nama,email,no_telp, No_SIP,gelar,spesialisasi, jenis_kelamin):
        super().__init__(username,password,nama,email,no_telp)
        self.No_STP = No_SIP
        self.gelar = gelar
        self.spesialis = spesialisasi
        self.jenis_kelamin = jenis_kelamin
        sql = "INSERT INTO dokter (username, password, nama, email,  no_telp, no_sip, gelar, spesialisasi, jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.username,self.password,self.nama,self.email,self.no_telp,self.No_STP,self.gelar,self.spesialis, self.jenis_kelamin)
        cursor.execute(sql, val)
    def Hapus_Dokter(self, nama):
        sql = "DELETE FROM dokter WHERE username=%s"
        val = (nama,)
        cursor.execute(sql, val)
    def List_Dokter(self):
        sql = "SELECT nama, email, no_telp, no_sip, gelar, spesialisasi, jenis_kelamin FROM dokter"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

class Pasien(Person):
    def Tambah_Pasien(self,username,password,nama,email,no_telp,tgl_lahir,jenis_kelamin):
        super().__init__(username,password,nama,email,no_telp)
        self.tgl_lahir = tgl_lahir
        self.jenis_kelamin = jenis_kelamin
        sql = "INSERT INTO pasien (username, password, nama, email, no_telp, tgl_lahir, jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.username, self.password, self.nama, self.email, self.no_telp, self.tgl_lahir, self.jenis_kelamin)
        cursor.execute(sql, val)
    def Hapus_Pasien(self,nama):
        sql = "DELETE FROM pasien WHERE username=%s"
        val = (nama,)
        cursor.execute(sql, val)
    def List_Pasien(self):
        sql = "SELECT * FROM pasien"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

class Admin(Person):
    def Tambah_Admin(self, username, password, nama, email ,no_telp):
        super().__init__(username,password,nama,email,no_telp)
        sql = "INSERT INTO admin (username, password, nama, email, no_telp) VALUES (%s, %s, %s, %s, %s)"
        val = (self.username, self.password, self.nama, self.email, self.no_telp)
        cursor.execute(sql, val)
    def Hapus_Admin(self,nama):
        sql = "DELETE FROM admin WHERE username=%s"
        val = (nama,)
        cursor.execute(sql, val)

class Jadwal_Praktik_Window (object):
    def setupUi(self, MainWindow):
        self.window = MainWindow

        self.pilihan = QComboBox(objectName="Menu")
        self.pilihan.addItem('.:: Pilih User ::.')
        self.pilihan.addItem('Admin')
        self.pilihan.addItem('Dokter')
        self.pilihan.addItem('Pasien')

        self.tombol1 = QPushButton('List')
        self.tombol1.setFixedSize(150, 50)
        self.tombol1.clicked.connect(self.list_user)
        self.tombol2 = QPushButton('Tambah')
        self.tombol2.setFixedSize(150, 50)
        self.tombol2.clicked.connect(self.tambah_user)
        self.tombol3 = QPushButton('Hapus')
        self.tombol3.setFixedSize(150, 50)
        self.tombol3.clicked.connect(self.hapus_user)
        self.tombol4 = QPushButton()

        self.label = QLabel('Username : ')
        self.username = QTextEdit()
        self.username.setFixedSize(181, 31)

        self.label2 = QLabel('Password : ')
        self.password = QTextEdit()
        self.password.setFixedSize(181, 31)

        self.label3 = QLabel('Nama : ')
        self.nama = QTextEdit()
        self.nama.setFixedSize(181, 31)

        self.label4 = QLabel('Email : ')
        self.email = QTextEdit()
        self.email.setFixedSize(181, 31)

        self.label5 = QLabel('No Telp : ')
        self.no_telp = QTextEdit()
        self.no_telp.setFixedSize(181, 31)

        self.label6 = QLabel()
        self.data6 = QTextEdit()
        self.data6.setFixedSize(181, 31)

        self.label7 = QLabel()
        self.data7 = QTextEdit()
        self.data7.setFixedSize(181, 31)

        self.label8 = QLabel()
        self.data8 = QTextEdit()
        self.data8.setFixedSize(181, 31)

        self.label9 = QLabel()
        self.data9 = QTextEdit()
        self.data9.setFixedSize(181, 31)

        self.label10 = QPlainTextEdit()
        self.label10.setReadOnly(True)

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.tombol1)
        self.horizontal.addWidget(self.tombol2)
        self.horizontal.addWidget(self.tombol3)

        self.horizontal2 = QHBoxLayout()
        self.horizontal3 = QHBoxLayout()
        self.horizontal4 = QHBoxLayout()
        self.horizontal5 = QHBoxLayout()
        self.horizontal6 = QHBoxLayout()
        self.horizontal7 = QHBoxLayout()
        self.horizontal8 = QHBoxLayout()
        self.horizontal9 = QHBoxLayout()

        self.vertikal = QVBoxLayout()
        self.vertikal.addWidget(self.pilihan)
        self.vertikal.addLayout(self.horizontal)
        self.vertikal.addLayout(self.horizontal2)
        self.vertikal.addLayout(self.horizontal3)
        self.vertikal.addLayout(self.horizontal4)
        self.vertikal.addLayout(self.horizontal5)
        self.vertikal.addLayout(self.horizontal6)
        self.vertikal.addLayout(self.horizontal7)
        self.vertikal.addLayout(self.horizontal8)
        self.vertikal.addLayout(self.horizontal9)

        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        MainWindow.setCentralWidget(self.widget)
        MainWindow.setWindowTitle("Admin - PsyCare")
        MainWindow.setGeometry(450, 300, 500, 120)

    def list_user(self):
        self.pilihan.close(), self.tombol1.close(), self.tombol2.close(), self.tombol3.close()
        self.label10.setFixedSize(600, 350)
        self.vertikal.addWidget(self.label10)
        cek = self.pilihan.currentText()
        if cek == "Dokter":
            data = Dokter()
            data2 = data.List_Dokter()
            self.label10.clear()
            for i in data2:
                self.label10.appendPlainText(str(i))
        elif cek == "Pasien":
            data = Pasien()
            data2 = data.List_Pasien()
            self.label10.clear()
            for i in data2:
                self.label10.appendPlainText(str(i))
        else:
            self.label10.clear()
            self.label10.insertPlainText("NONE")

    def tambah_user(self):
        self.pilihan.close(), self.tombol1.close(), self.tombol2.close(), self.tombol3.close()
        cek = self.pilihan.currentText()
        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.username)
        self.horizontal2.addWidget(self.label2), self.horizontal2.addWidget(self.password)
        self.horizontal3.addWidget(self.label3), self.horizontal3.addWidget(self.nama)
        self.horizontal4.addWidget(self.label4), self.horizontal4.addWidget(self.email)
        self.horizontal5.addWidget(self.label5), self.horizontal5.addWidget(self.no_telp)
        if cek == "Dokter":
            self.label6.setText('No SIP : ')
            self.label7.setText('Gelar : ')
            self.label8.setText('Spesialisasi : ')
            self.label9.setText('Jenis Kelamin (L/P) : ')
            self.horizontal6.addWidget(self.label6), self.horizontal6.addWidget(self.data6)
            self.horizontal7.addWidget(self.label7), self.horizontal7.addWidget(self.data7)
            self.horizontal8.addWidget(self.label8), self.horizontal8.addWidget(self.data8)
            self.horizontal9.addWidget(self.label9), self.horizontal9.addWidget(self.data9)
            self.tombol4.clicked.connect(self.tambah_dokter)
        elif cek == "Pasien":
            self.label6.setText('Tanggal Lahir : ')
            self.label7.setText('Jenis Kelamin (L/P) : ')
            self.horizontal6.addWidget(self.label6), self.horizontal6.addWidget(self.data6)
            self.horizontal7.addWidget(self.label7), self.horizontal7.addWidget(self.data7)
            self.tombol4.clicked.connect(self.tambah_pasien)
        elif cek == "Admin":
            self.tombol4.clicked.connect(self.tambah_admin)
        self.tombol4.setText('Add')
        self.vertikal.addWidget(self.tombol4)

    def hapus_user(self):
        self.pilihan.close(), self.tombol1.close(), self.tombol2.close(), self.tombol3.close()
        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.username)
        cek = self.pilihan.currentText()
        if cek == "Admin":
            self.tombol4.clicked.connect(self.hapus_admin)
        elif cek == "Pasien":
            self.tombol4.clicked.connect(self.hapus_pasien)
        if cek == "Dokter":
            self.tombol4.clicked.connect(self.hapus_dokter)
        self.tombol4.setText('Delete')
        self.vertikal.addWidget(self.tombol4)

    def data(self):
        self.username2 = self.username.toPlainText()
        self.password2 = self.password.toPlainText()
        self.nama2 = self.nama.toPlainText()
        self.email2 = self.email.toPlainText()
        self.no_telp2 = self.no_telp.toPlainText()
        self.data6_2 = self.data6.toPlainText()
        self.data7_2 = self.data7.toPlainText()
        self.data8_2 = self.data8.toPlainText()
        self.data9_2 = self.data9.toPlainText()

    def tambah_admin(self):
        self.data()
        data2 = Admin()
        data2.Tambah_Admin(self.username2, self.password2, self.nama2, self.email2, self.no_telp2)
        MainWindow.close()

    def tambah_pasien(self):
        self.data()
        data2 = Pasien()
        data2.Tambah_Pasien(self.username2,self.password2, self.nama2, self.email2, self.no_telp2, self.data6_2, self.data7_2)
        MainWindow.close()

    def tambah_dokter(self):
        self.data()
        data2 = Dokter()
        data2.Tambah_Dokter(self.username2,self.password2, self.nama2, self.email2, self.no_telp2, self.data6_2, self.data7_2, self.data8_2, self.data9_2)
        MainWindow.close()

    def hapus_admin(self):
        self.data()
        data2 = Admin()
        data2.Hapus_Admin(self.username2)
        MainWindow.close()

    def hapus_dokter(self):
        self.data()
        data2 = Dokter()
        data2.Hapus_Dokter(self.username2)
        MainWindow.close()

    def hapus_pasien(self):
        self.data()
        data2 = Pasien()
        data2.Hapus_Pasien(self.username2)
        MainWindow.close()

db.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    MainWindow = QMainWindow()
    ui = Jadwal_Praktik_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())