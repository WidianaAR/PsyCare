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

class Info:
    def __init__(self, nama):
        self.nama = nama
    def Tambah_Info(self, judul, isi_info):
        self.judul = judul
        self.isi_info = isi_info
        sql = "INSERT INTO info (nama, judul, isi_info) VALUES (%s, %s, %s)"
        val = (self.nama, self.judul, self.isi_info)
        cursor.execute(sql, val)

class Jadwal_Praktik_Window (object):
    def setupUi(self, MainWindow):
        self.window = MainWindow

        self.label = QLabel('Judul : ')
        self.judul = QTextEdit()
        self.judul.setFixedSize(181, 31)

        self.label2 = QLabel('Isi : ')
        self.isi = QTextEdit()
        self.isi.setFixedSize(350, 300)

        self.label3 = QLabel("Nama Admin : ")
        self.nama = QTextEdit()
        self.nama.setFixedSize(181, 31)

        self.add = QPushButton()
        self.add.setFixedSize(QSize(150, 50))
        self.add.setText("Tambah")
        self.add.clicked.connect(self.tambah)

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.label3)
        self.horizontal.addWidget(self.nama)
        
        self.horizontal2 = QHBoxLayout()
        self.horizontal2.addWidget(self.label)
        self.horizontal2.addWidget(self.judul)

        self.horizontal3 = QHBoxLayout()
        self.horizontal3.addWidget(self.label2)
        self.horizontal3.addWidget(self.isi)

        self.vertikal = QVBoxLayout()
        self.vertikal.addLayout(self.horizontal)
        self.vertikal.addLayout(self.horizontal2)
        self.vertikal.addLayout(self.horizontal3)
        self.vertikal.addWidget(self.add)

        self.widget = QWidget()
        self.widget.setLayout(self.vertikal)
        MainWindow.setCentralWidget(self.widget)
        MainWindow.setWindowTitle("Tambah Info")
        MainWindow.setGeometry(450, 180, 500, 120)

    def data(self):
        self.nama2 = self.nama.toPlainText()
        self.judul2 = self.judul.toPlainText()
        self.isi2 = self.isi.toPlainText()

    def tambah(self):
        self.data()
        info = Info(self.nama2)
        info.Tambah_Info(self.judul2, self.isi2)
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