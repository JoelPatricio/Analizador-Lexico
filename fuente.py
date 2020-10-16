from PyQt5.QtCore import QFile, QIODevice, Qt, QRect, QSize
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from ventana1 import *
from PyQt5.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit, QMainWindow, QAction, qApp, QApplication)
from PyQt5.QtGui import QColor, QPainter, QTextFormat, QKeySequence, QFont


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        header = self.tableWidget.horizontalHeader()  
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.pushButton_2.clicked.connect(self.cargarArchivo)
        self.pushButton.clicked.connect(self.iniciar)
        
        columna=self.tableWidget.insertRow(self.tableWidget.rowCount())        
        item1=QTableWidgetItem("Palabra Reservada")
        item2 = QTableWidgetItem("while")
        self.tableWidget.setItem(0, 0, item1)
        self.tableWidget.setItem(0, 1, item2)
        

    def cargarArchivo(self):
        self.plainTextEdit.clear()
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])        
        contenido=open(archivo,'r')
        linea=""
        texto=''
        for linea in contenido.readlines():
            texto =texto.__add__(linea)
        contenido.close()
        textoAux=''
        for linea in range(3,len(texto)):
            textoAux = textoAux.__add__(texto[linea])            
        self.plainTextEdit.appendPlainText(textoAux)
        self.pushButton.setEnabled(True)
        pass

    def iniciar(self):
        palabrasReservadas=[]
        
        
        pass


    


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
