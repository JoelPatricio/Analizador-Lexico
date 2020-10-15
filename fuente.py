from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import QFileDialog
from ventana1 import *
import PyQt5.QtCore


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.cargarArchivo)
        self.pushButton.clicked.connect(self.iniciar)

    def cargarArchivo(self):
        self.plainTextEdit.clear()
        archivo = QFileDialog.getOpenFileName(self)
        archivo = str(archivo[0])
        contenido=open(archivo,'r')
        for linea in contenido.readlines():
            self.plainTextEdit.appendPlainText(linea)
        contenido.close()
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
