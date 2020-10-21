from PyQt5.QtCore import QFile, QIODevice, Qt, QRect, QSize
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from ventana1 import *
from PyQt5.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit, QMainWindow, QAction, qApp, QApplication)
from PyQt5.QtGui import QColor, QPainter, QTextFormat, QKeySequence, QFont
import re


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
        header=self.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)

        self.pushButton_2.clicked.connect(self.cargarArchivo)
        self.pushButton_3.clicked.connect(self.leerAutomata)        
        self.pushButton_4.clicked.connect(self.cargarPalabrasReservadas)
        self.pushButton.clicked.connect(self.iniciarAnalisis)

        
        #columna=self.tableWidget.insertRow(self.tableWidget.rowCount())        
        #item1=QTableWidgetItem("Palabra Reservada")
        #item2 = QTableWidgetItem("while")
        #self.tableWidget.setItem(0, 0, item1)
        #self.tableWidget.setItem(0, 1, item2)
        

    def cargarArchivo(self):
        self.plainTextEdit.clear()
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])
        global textoAux
        contenidoTxt=open(archivo,'r')
        linea=""
        texto=''
        for linea in contenidoTxt.readlines():
            texto =texto.__add__(linea)
        contenidoTxt.close()
        textoAux=''
        for linea in range(3,len(texto)):
            textoAux = textoAux.__add__(texto[linea])            
        self.plainTextEdit.appendPlainText(textoAux)
        self.pushButton.setEnabled(True)
        pass

    def leerEstadosFinales(self,linea):
        estadosf=linea
        estadosf=estadosf.replace('\n','')
        estadosf=estadosf.split(',')
        global estadosFinales
        global retroceso
        estadosFinales=[]
        retroceso=[]
        for x in estadosf:
            x=x.split(':')
            #x[2]=x[2].replace('\n','')
            estadosFinales.append(dict.fromkeys(x[0],x[1]))
            retroceso.append(dict.fromkeys(x[0],x[2]))
        pass

    def crearAutomata(self,linea):
        linea=linea.replace('\n','')
        linea=linea.split(',')
        estadoN=[]
        for x in linea:
            x=x.split(':')
            estadoN.append(dict.fromkeys(x[0],x[1]))
        return estadoN
        pass

    def leerAutomata(self):
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])
        contenido = open(archivo, 'r')
        global tablaTransicion
        tablaTransicion=[]
        primeraLinea=True
        for linea in contenido.readlines():
            if(primeraLinea==True):
                print(linea)
                self.leerEstadosFinales(linea)
                primeraLinea=False
            else:
                linea = linea.split("==>")
                tablaTransicion.append(dict.fromkeys(linea[0],self.crearAutomata(linea[1])))
        contenido.close()
        print(estadosFinales)
        print(retroceso)
        print(tablaTransicion)
        pass

    def cargarPalabrasReservadas(self):
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])        
        contenido=open(archivo,'r')
        global palabrasReservadas
        palabrasReservadas = []
        for linea in contenido.readlines():
            linea=linea.rstrip('\n')
            palabrasReservadas.append(linea)
            columna=self.tableWidget_3.insertRow(self.tableWidget.rowCount())        
            item1=QTableWidgetItem(linea)
            self.tableWidget_3.setItem(0, 0, item1)
        contenido.close()
        pass

    def buscarEstado(self,letra,estadoInicial,posicion):
        
        pass

    def iniciarAnalisis(self):
        tam=len(textoAux)
        i=0
        while(i<tam):
            buscarEstado(textoAux[i],0,i)
            



            i=i+1

        pass
    


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
