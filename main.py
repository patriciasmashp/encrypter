# Form implementation generated from reading ui file 'crypto.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from math import ceil, sqrt
from turtle import width
from PyQt6 import QtCore, QtGui, QtWidgets
import crypto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.idents = QtWidgets.QSpinBox(self.centralwidget)
        self.idents.setObjectName("idents")
        self.idents.setMinimum(1)
        self.gridLayout.addWidget(self.idents, 1, 4, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 2, 1)
        self.width_label = QtWidgets.QLabel(self.centralwidget)
        self.width_label.setObjectName("width_label")

        self.gridLayout.addWidget(self.width_label, 0, 1, 1, 1)
        self.height_label = QtWidgets.QLabel(self.centralwidget)
        self.height_label.setObjectName("height_label")
        self.gridLayout.addWidget(self.height_label, 1, 1, 1, 1)
        self.height_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.height_spinBox.setMinimum(1)
        self.height_spinBox.setObjectName("height_spinBox")
        self.gridLayout.addWidget(self.height_spinBox, 1, 2, 1, 1)
        self.intedents_label = QtWidgets.QLabel(self.centralwidget)
        self.intedents_label.setObjectName("intedents_label")
        self.gridLayout.addWidget(self.intedents_label, 1, 3, 1, 1)
        self.width_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.width_spinBox.setObjectName("width_spinBox")
        self.width_spinBox.setMinimum(1)
        self.gridLayout.addWidget(self.width_spinBox, 0, 2, 1, 1)
        self.transfer_label = QtWidgets.QLabel(self.centralwidget)
        self.transfer_label.setObjectName("transfer_label")
        self.gridLayout.addWidget(self.transfer_label, 0, 3, 1, 1)
        self.transfer_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.transfer_spinBox.setObjectName("transfer_spinBox")
        self.transfer_spinBox.setMinimum(1)
        self.gridLayout.addWidget(self.transfer_spinBox, 0, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "encrypter"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.width_label.setText(_translate("MainWindow", "Ширина"))
        self.height_label.setText(_translate("MainWindow", "Высота"))
        self.intedents_label.setText(_translate("MainWindow", "Отступы"))
        self.transfer_label.setText(_translate("MainWindow", "Перенос"))
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))

    def add_functions(self):
        
        self.pushButton.clicked.connect(self.app)
        
    def getConfig(self):
        width = self.width_spinBox.value()
        height = self.height_spinBox.value()
        idents = self.idents.value()
        transfers = self.transfer_spinBox.value()

        return {
            'size':{
                'height': height,
                'width': width
                },
            'idents': idents,
            'transfers': transfers
        }
    


    def setMinSquareSize(self):
        minSize = ceil(sqrt(len(self.getText())))
        self.width_spinBox.setValue(minSize)
        self.height_spinBox.setValue(minSize)
        

    def validateConfig(self):
        config = self.getConfig()
        width = config['size']['width']
        height = config['size']['height']
        text = self.getText()

        if len(text)/height > width:
            print('setting up min size')
            self.setMinSquareSize()
        

    def getText(self):
        return self.textEdit.toPlainText()

    def app(self):
        ct = ''
        text = self.getText()
        self.validateConfig()
        
        res = crypto.encrypt(text, self.getConfig())
        for row in res:
            ct += ''.join(row).replace(' ','')
        
        self.textBrowser.setText(ct)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
