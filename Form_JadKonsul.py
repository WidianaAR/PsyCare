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

class Jadwal_Konsul:
    def __init__(self, nama_dokter_dokter=None, nama_dokter_pasien=None):
        self.nama_dokter_dokter = nama_dokter_dokter
        self.nama_dokter_pasien = nama_dokter_pasien
    def Tambah_Jadwal(self, tanggal, keterangan):
        self.tanggal = tanggal
        self.keterangan = keterangan
        sql = "INSERT INTO jadwal_konsul (dokter, pasien, tanggal, keterangan) VALUES (%s, %s, %s, %s)"
        val = (self.nama_dokter_dokter, self.nama_dokter_pasien, self.tanggal, self.keterangan)
        cursor.execute(sql, val)
    def Hapus_Jadwal(self, tanggal):
        sql = "DELETE FROM jadwal_konsul WHERE dokter='{}' AND tanggal='{}'".format(self.nama_dokter_dokter,tanggal)
        cursor.execute(sql)

class Jadwal_Praktik_Window (object):
    def setupUi(self, MainWindow):
        self.window = MainWindow

        self.label = QLabel('Nama Dokter: ')
        self.nama_dokter = QTextEdit()
        self.nama_dokter.setFixedSize(181, 31)

        self.label2 = QLabel('Nama Pasien : ')
        self.nama_pasien = QTextEdit()
        self.nama_pasien.setFixedSize(181, 31)

        self.label3 = QLabel('Tanggal : ')
        self.tanggal = QTextEdit()
        self.tanggal.setFixedSize(181, 31)

        self.label4 = QLabel('Keterangan : ')
        self.keterangan = QTextEdit()
        self.keterangan.setFixedSize(181, 31)

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
        MainWindow.setWindowTitle("Form Jadwal Konsul")
        MainWindow.resize(170, 250)

    def data(self):
        self.nama_dokter2 = self.nama_dokter.toPlainText()
        self.nama_pasien2 = self.nama_pasien.toPlainText()
        self.tanggal2 = self.tanggal.toPlainText()
        self.keterangan2 = self.keterangan.toPlainText()
        self.data2 = Jadwal_Konsul(self.nama_dokter2, self.nama_pasien2)

    def form_tambah(self):
        MainWindow.setFixedSize(300, 400)
        self.add.hide(), self.delete.hide()
        self.tombol.setText('Add')
        self.tombol.clicked.connect(self.Tambahkan)

        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.nama_dokter)
        self.horizontal1.addWidget(self.label2), self.horizontal1.addWidget(self.nama_pasien)
        self.horizontal2.addWidget(self.label3), self.horizontal2.addWidget(self.tanggal)
        self.horizontal3.addWidget(self.label4), self.horizontal3.addWidget(self.keterangan)

        self.vertikal2.addWidget(self.tombol)

    def Tambahkan(self):
        self.data()
        self.data2.Tambah_Jadwal(self.tanggal2, self.keterangan2)
        self.window.close()

    def form_hapus(self):
        MainWindow.setFixedSize(300, 400)
        self.add.hide(), self.delete.hide()
        self.tombol.setText('Delete')
        self.tombol.clicked.connect(self.Hapus_Data)

        self.horizontal.addWidget(self.label), self.horizontal.addWidget(self.nama_dokter)
        self.horizontal1.addWidget(self.label3), self.horizontal1.addWidget(self.tanggal)

        self.vertikal2.addWidget(self.tombol)

    def Hapus_Data(self):
        self.data()
        self.data2.Hapus_Jadwal(self.tanggal2)
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