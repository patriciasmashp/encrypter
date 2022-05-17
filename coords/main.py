from ui import Ui_MainWindow
from crypto import algo
from PyQt6 import QtCore, QtGui, QtWidgets
import ctypes

class Apllication(Ui_MainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setObjectName("encoder")
        super().setupUi(MainWindow)

    def __init__(self) -> None:
        
        myappid = 'encoder64'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        super().__init__()
        
    def add_functions(self):
        self.lineEdit.setEnabled(False)
        self._setRegex(r"\d\d.\d\d\d\d")
        self.pushButton.clicked.connect(self.app)
        self.comboBox.activated.connect(self.list_changed)

    def list_changed(self, i):
        if self.comboBox.currentText() == 'Задать шаблон':
            self.lineEdit.setEnabled(True)
            self._setRegex("")
        elif self.comboBox.currentText() == 'Координаты':
            self.lineEdit.setEnabled(False)
            self._setRegex(r"\d\d.\d\d\d\d")
        else:
            self.lineEdit.setEnabled(False)
            

    def app(self):
        self.textBrowser.setText(algo(self.getConfig(), self.getText())) 

    def getConfig(self):
       return { 
           'idents':self.spinBox.value(),
            'regex': self.lineEdit.text()
       }
       
    def getText(self):
        return self.plainTextEdit.toPlainText()

    def _setRegex(self, regex):
        self.lineEdit.setText(regex)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Apllication()
    ui.setupUi(MainWindow)
    ui.add_functions()
    MainWindow.show()
    sys.exit(app.exec())
