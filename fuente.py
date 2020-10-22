from os import times
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
        estadosFinales={}
        retroceso={}
        for x in estadosf:
            x=x.split(':')
            estadosFinales[x[0]]=x[1]
            retroceso[x[0]]=x[2]
        pass

    def crearAutomata(self,linea):
        linea=linea.replace('\n','')
        linea=linea.split('=>')
        estadoN={}
        for x in linea:
            x=x.split(':')
            estadoN[x[0]]=x[1]
        return estadoN
        pass

    def leerAutomata(self):
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])
        contenido = open(archivo, 'r')
        global tablaTransicion
        tablaTransicion={}
        primeraLinea=True
        for linea in contenido.readlines():
            if(primeraLinea==True):
                print(linea)
                self.leerEstadosFinales(linea)
                primeraLinea=False
            else:
                linea = linea.split("==>")
                tablaTransicion[linea[0]]=self.crearAutomata(linea[1])
        contenido.close()
        print(retroceso)
        pass

    def cargarPalabrasReservadas(self):
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])        
        contenido=open(archivo,'r')
        global palabrasReservadas
        palabrasReservadas = {}
        for linea in contenido.readlines():
            linea=linea.rstrip('\n')
            palabrasReservadas[linea]=linea
            filas=self.tableWidget_3.rowCount()
            columna=self.tableWidget_3.insertRow(filas)
            item1=QTableWidgetItem(linea)
            self.tableWidget_3.setItem(filas, 0, item1)
        contenido.close()
        print(palabrasReservadas)
        pass

    def crearEstado(self, cadena,estado):
        print("Creando estado")
        try:
            if(palabrasReservadas[cadena]):
                filas = self.tableWidget.rowCount()
                columna = self.tableWidget.insertRow(filas)
                item1 = QTableWidgetItem("Palabra Reservada")
                item2 = QTableWidgetItem(cadena)
                self.tableWidget.setItem(filas, 0, item1)
                self.tableWidget.setItem(filas, 1, item2)
        except KeyError:
            filas = self.tableWidget.rowCount()
            columna = self.tableWidget.insertRow(filas)
            item1 = QTableWidgetItem(estado)
            item2 = QTableWidgetItem(cadena)
            self.tableWidget.setItem(filas, 0, item1)
            self.tableWidget.setItem(filas, 1, item2)
        pass

    def buscarEstado(self,caracter,estadoInicial,posicion,cadena):
        global errorReturn
        print("Valor Evaluar: "+caracter)        
        estadoInicial=str(estadoInicial)
        cadena=str(cadena)
        if(caracter!=" " and textoAux[posicion]!=";"):
            try:
                if(estadosFinales[estadoInicial]):
                    print("Cadena: "+cadena+":")
                    print("Estado final: "+estadosFinales[estadoInicial])
                    print("Retroceso: "+retroceso[estadoInicial])
                    self.crearEstado(cadena, estadosFinales[estadoInicial])
                    pos = posicion
                    retro = retroceso[estadoInicial]
                    retro = int(retro)
                    aux = int(pos-retro)
                    print("========")
                    print(aux)
                    errorReturn = aux
            except KeyError:
                if(caracter.isdigit()):
                    print(tablaTransicion[estadoInicial]["dig"])
                    if(tablaTransicion[estadoInicial]["dig"] != "-"):
                        self.buscarEstado(textoAux[posicion+1], tablaTransicion[estadoInicial]["dig"], posicion+1, cadena+str(textoAux[posicion]))
                elif(re.search(r"[aA-zZ]", caracter) != None and caracter != " "):
                    print(tablaTransicion[estadoInicial]["let"])
                    if(tablaTransicion[estadoInicial]["let"] != "-"):
                        self.buscarEstado(textoAux[posicion+1], tablaTransicion[estadoInicial]["let"], posicion+1, cadena+str(textoAux[posicion]))
                elif(tablaTransicion[estadoInicial][caracter] != "-"):
                    self.buscarEstado(textoAux[posicion+1], tablaTransicion[estadoInicial][caracter], posicion+1, cadena+str(textoAux[posicion]))
                elif(tablaTransicion[estadoInicial]["otro"] != "-"):
                    self.buscarEstado(textoAux[posicion], tablaTransicion[estadoInicial]["otro"], posicion, cadena)
                else:
                    errorReturn = -1
                    print(errorReturn)
        else:
            if(caracter==" "):
                self.buscarEstado(textoAux[posicion+1], tablaTransicion[estadoInicial]["otro"], posicion, cadena)
            else:
                errorReturn = -2
                #self.buscarEstado(textoAux[posicion], tablaTransicion[estadoInicial]["otro"], posicion, cadena)
        return errorReturn

    def iniciarAnalisis(self):
        i=0
        while(i<len(textoAux)):
            if(textoAux[i]==" "):
                i=i+1
                pass

            estado=self.buscarEstado(textoAux[i],0,i,"")
            print("ES el estado return: "+str(estado))
            if(estado==-1):
                filas = self.tableWidget_2.rowCount()
                columna = self.tableWidget_2.insertRow(filas)
                aux = "Posición: "+str(i)
                aux2 = "No hay enlace con caracter: "+str(textoAux[i])
                item1 = QTableWidgetItem(aux)
                item2 = QTableWidgetItem(aux2)
                self.tableWidget_2.setItem(filas, 0, item1)
                self.tableWidget_2.setItem(filas, 1, item2)
                i = i+1
            elif(estado == -2):
                break
            else:
                print("------------------")
                print(estado)
                i=estado
                i=int(i)
                i=i+1

        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
