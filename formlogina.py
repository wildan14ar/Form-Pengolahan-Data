# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formlogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formlogin(object):
    def setupUi(self, Formlogin):
        Formlogin.setObjectName("Formlogin")
        Formlogin.resize(517, 455)
        self.widget = QtWidgets.QWidget(Formlogin)
        self.widget.setGeometry(QtCore.QRect(10, 10, 491, 431))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 431))
        self.label.setStyleSheet("background-color: rgb(121, 156, 191);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_login = QtWidgets.QPushButton(self.widget)
        self.pushButton_login.setGeometry(QtCore.QRect(90, 300, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QpushButton#pushButton{\n"
"background-color: rgb(255, 0, 118);\n"
"color: rgb(255, 0, 118);\n"
"border-radius: 5px;\n"
"}\n"
"QpushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgb(255, 0, 118)\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QpushButton#pushButton:hover{\n"
"background-color: rgb(255, 0, 118)\n"
"}\n"
"\n"
"")
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_loginform = QtWidgets.QLabel(self.widget)
        self.label_loginform.setGeometry(QtCore.QRect(120, 50, 251, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 44, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_loginform.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_loginform.setFont(font)
        self.label_loginform.setStyleSheet("color:rgb(28, 28, 28)")
        self.label_loginform.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loginform.setObjectName("label_loginform")
        self.label_forgot = QtWidgets.QLabel(self.widget)
        self.label_forgot.setGeometry(QtCore.QRect(110, 370, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        self.label_forgot.setFont(font)
        self.label_forgot.setStyleSheet("color: rgb(28, 28, 28);")
        self.label_forgot.setObjectName("label_forgot")
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username.setGeometry(QtCore.QRect(90, 150, 311, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_username.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("background-color: rgb(121, 156, 191);\n"
"border:1px solid rgb(121, 156, 191);\n"
"border-bottom-color: rgb(45, 70, 129);\n"
"padding-bottom: 9px;\n"
"color: rgb(28, 28, 28);")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.pushButton_SignIn = QtWidgets.QPushButton(self.widget)
        self.pushButton_SignIn.setGeometry(QtCore.QRect(290, 300, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SignIn.setFont(font)
        self.pushButton_SignIn.setStyleSheet("QpushButton#pushButton{\n"
"background-color: rgb(255, 0, 118);\n"
"color: rgb(255, 0, 118);\n"
"border-radius: 5px;\n"
"}\n"
"QpushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgb(255, 0, 118)\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"QpushButton#pushButton:hover{\n"
"background-color: rgb(255, 0, 118)\n"
"}\n"
"\n"
"")
        self.pushButton_SignIn.setObjectName("pushButton_SignIn")
        self.lineEdit_username_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username_3.setGeometry(QtCore.QRect(90, 210, 311, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 156, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_username_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        self.lineEdit_username_3.setFont(font)
        self.lineEdit_username_3.setStyleSheet("background-color: rgb(121, 156, 191);\n"
"border:1px solid rgb(121, 156, 191);\n"
"border-bottom-color: rgb(45, 70, 129);\n"
"padding-bottom: 9px;")
        self.lineEdit_username_3.setText("")
        self.lineEdit_username_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_username_3.setObjectName("lineEdit_username_3")

        self.retranslateUi(Formlogin)
        QtCore.QMetaObject.connectSlotsByName(Formlogin)

    def retranslateUi(self, Formlogin):
        _translate = QtCore.QCoreApplication.translate
        Formlogin.setWindowTitle(_translate("Formlogin", "Form"))
        self.pushButton_login.setText(_translate("Formlogin", "LOGIN"))
        self.label_loginform.setText(_translate("Formlogin", "Log-In Form"))
        self.label_forgot.setText(_translate("Formlogin", "Forgot your Username or Password?"))
        self.lineEdit_username.setPlaceholderText(_translate("Formlogin", "  Username"))
        self.pushButton_SignIn.setText(_translate("Formlogin", "GUEST"))
        self.lineEdit_username_3.setPlaceholderText(_translate("Formlogin", "  password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formlogin = QtWidgets.QWidget()
    ui = Ui_Formlogin()
    ui.setupUi(Formlogin)
    Formlogin.show()
    sys.exit(app.exec_())