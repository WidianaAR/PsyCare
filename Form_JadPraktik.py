from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

class Jadwal_Praktik():
    def __init__(self, nama_dokter):
        self.nama_dokter = nama_dokter
    def add_Jadwal(self, hari, jam_awal, jam_akhir):
        self.hari = hari
        self.jam_awal = jam_awal
        self.jam_akhir = jam_akhir
        sql = "INSERT INTO jadwal_praktik (nama_dokter, hari, jam_awal, jam_akhir) VALUES (%s, %s, %s, %s)"
        val = (self.nama_dokter, self.hari, self.jam_awal, self.jam_akhir)
        cursor.execute(sql, val)
    def Hapus_Jadwal(self, hari):
        sql = "DELETE FROM jadwal_praktik WHERE nama_dokter='{}' AND hari='{}'".format(self.nama_dokter,hari)
        cursor.execute(sql)

class Jadwal_Praktik_Window (object):
    def setupUi(self, MainWindow):
        self.window = MainWindow

        self.label = QLabel('Nama : ')
        self.nama = QTextEdit()
        self.nama.setFixedSize(181, 31)

        self.label2 = QLabel('Hari : ')
        self.hari = QTextEdit()
        self.hari.setFixedSize(181, 31)

        self.label3 = QLabel('Jam Awal (00.00) : ')
        self.jam_awal = QTextEdit()
        self.jam_awal.setFixedSize(181, 31)

        self.label4 = QLabel('Jam Akhir (00.00) : ')
        self.jam_akhir = QTextEdit()
        self.jam_akhir.setFixedSize(181, 31)

        self.add = QPushButton()
        self.add.setFixedSize(QSize(150, 50))
        self.add.setText("Tambah")
        self.add.clicked.connect(self.form_tambah)

        self.delete = QPushButton()
        self.delete.setFixedSize(QSize(150, 50))
        self.delete.setText("Hapus")
        self.delete.clicked.connect(self.form_hapus)

        self.tombol = QPushButton()
        self.tombol.setFixedSize(QSize(218, 30))

        self.horizontal = QHBoxLayout()
        self.horizontal1 = QHBoxLayout()
        self.horizontal2 = QHBoxLayout()
        self.horizontal3 = QHBoxLayout()

        self.vertikal2 = QVBoxLayout()
        self.vertikal2.addLayout(self.horizontal)
        self.vertikal2.addLayout(self.horizontal1)
        self.vertikal2.addLayout(self.horizontal2)
        self.vertikal2.addLayout(self.horizontal3)
        self.vertikal2.addWidget(self.add)
        self.vertikal2.addWidget(self.delete)

        self.widget = QWidget()
        self.widget.setLayout(self.vertikal2)
        MainWindow.setCentralWidget(self.widget)
        MainWindow.setWindowTitle("Form Jadwal Praktik")
        MainWindow.resize(170, 250)

    def data(self):
        self.nama2 = self.nama.toPlainText()
        self.hari2 = self.hari.toPlainText()
        self.jam_awal2 = self.jam_awal.toPlainText()
        self.jam_akhir2 = self.jam_akhir.toPlainText()
        self.data2 = Jadwal_Praktik(self.nama2)

    def form_tambah(self):
        MainWindow.setFixedSize(350, 400)
        self.add.hide(), self.delete.hide()
        self.tombol.setText('Add')
        self.tombol.clicked.connect(self.Tambahkan)

        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.nama)
        self.horizontal1.addWidget(self.label2), self.horizontal1.addWidget(self.hari)
        self.horizontal2.addWidget(self.label3), self.horizontal2.addWidget(self.jam_awal)
        self.horizontal3.addWidget(self.label4), self.horizontal3.addWidget(self.jam_akhir)

        self.vertikal2.addWidget(self.tombol)

    def Tambahkan(self):
        self.data()
        self.data2.add_Jadwal(self.hari2, self.jam_awal2, self.jam_akhir2)
        self.window.close()

    def form_hapus(self):
        MainWindow.setFixedSize(300, 400)
        self.add.hide(), self.delete.hide()
        self.tombol.setText('Delete')
        self.tombol.clicked.connect(self.Hapus_Data)

        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.nama)
        self.horizontal1.addWidget(self.label2), self.horizontal1.addWidget(self.hari)

        self.vertikal2.addWidget(self.tombol)

    def Hapus_Data(self):
        self.data()
        self.data2.Hapus_Jadwal(self.hari2)
        self.window.close()

db.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    MainWindow = QMainWindow()
    ui = Jadwal_Praktik_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())