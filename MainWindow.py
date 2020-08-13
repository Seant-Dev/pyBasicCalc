# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from smtplib import LMTP

from PyQt5.QtWidgets import QMessageBox

import designStyle as dS

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.entrada = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 247)
        MainWindow.setStyleSheet(dS.Style.cssPrincipal)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(11, 12, 181, 25))
        self.lineEdit.setStyleSheet(dS.Style.cssTexto)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(104, 43, 40, 25))
        self.pushButton_clear.setStyleSheet(dS.Style.cssAmarillo)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(58, 43, 40, 25))
        self.pushButton_back.setStyleSheet(dS.Style.cssAmarillo)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(11, 43, 41, 25))
        self.pushButton_close.setStyleSheet(dS.Style.cssCerrar)
        self.pushButton_close.setObjectName("pushButton_close")

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(11, 167, 41, 25))
        self.pushButton_0.setStyleSheet(dS.Style.cssNum)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(11, 136, 41, 25))
        self.pushButton_1.setStyleSheet(dS.Style.cssNum)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(58, 136, 40, 25))
        self.pushButton_2.setStyleSheet(dS.Style.cssNum)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(104, 136, 40, 25))
        self.pushButton_3.setStyleSheet(dS.Style.cssNum)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(11, 105, 41, 25))
        self.pushButton_4.setStyleSheet(dS.Style.cssNum)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(58, 105, 40, 25))
        self.pushButton_5.setStyleSheet(dS.Style.cssNum)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(104, 105, 40, 25))
        self.pushButton_6.setStyleSheet(dS.Style.cssNum)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(11, 74, 41, 25))
        self.pushButton_7.setStyleSheet(dS.Style.cssNum)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(58, 74, 40, 25))
        self.pushButton_8.setStyleSheet(dS.Style.cssNum)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(104, 74, 40, 25))
        self.pushButton_9.setStyleSheet(dS.Style.cssNum)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_sum = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sum.setGeometry(QtCore.QRect(150, 167, 40, 25))
        self.pushButton_sum.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_sum.setObjectName("pushButton_sum")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(150, 74, 40, 25))
        self.pushButton_div.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_prod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prod.setGeometry(QtCore.QRect(150, 105, 40, 25))
        self.pushButton_prod.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_prod.setObjectName("pushButton_prod")
        self.pushButton_res = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_res.setGeometry(QtCore.QRect(150, 136, 40, 25))
        self.pushButton_res.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_res.setObjectName("pushButton_res")
        self.pushButton_pow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pow.setGeometry(QtCore.QRect(150, 43, 40, 25))
        self.pushButton_pow.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_pow.setObjectName("pushButton_pow")

        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(58, 167, 40, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_dot.setObjectName("pushButton_dot")

        self.pushButton_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eq.setGeometry(QtCore.QRect(104, 167, 40, 25))
        self.pushButton_eq.setStyleSheet(dS.Style.cssFunciones)
        self.pushButton_eq.setObjectName("pushButton_eq")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 201, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLimpiar = QtWidgets.QAction(MainWindow)
        self.actionLimpiar.setObjectName("actionLimpiar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionLimpiar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_0.clicked.connect(lambda: self.valor(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.valor(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.valor(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.valor(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.valor(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.valor(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.valor(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.valor(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.valor(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.valor(self.pushButton_9.text()))
        self.pushButton_dot.clicked.connect(lambda: self.valor(self.pushButton_dot.text()))

        self.pushButton_div.clicked.connect(lambda: self.valor(self.pushButton_div.text()))
        self.pushButton_prod.clicked.connect(lambda: self.valor('*'))
        self.pushButton_res.clicked.connect(lambda: self.valor(self.pushButton_res.text()))
        self.pushButton_sum.clicked.connect(lambda: self.valor(self.pushButton_sum.text()))

        self.pushButton_pow.clicked.connect(self.valor_pow)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_eq.clicked.connect(self.eq)
        self.pushButton_close.clicked.connect(QtWidgets.qApp.exit)

        self.actionLimpiar.triggered.connect(self.clear)
        self.actionSalir.triggered.connect(QtWidgets.qApp.exit)
        self.actionAyuda.triggered.connect(self.ayuda)
        self.actionAcerca_de.triggered.connect(self.acerdaDe)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyBasicCalc"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clr"))
        self.pushButton_back.setText(_translate("MainWindow", "←"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.pushButton_pow.setText(_translate("MainWindow", "x²"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_prod.setText(_translate("MainWindow", "x"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_res.setText(_translate("MainWindow", "-"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_sum.setText(_translate("MainWindow", "+"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))

    def valor(self, valor):
        self.statusbar.showMessage("")
        self.entrada = self.lineEdit.text()
        self.entrada += valor
        self.lineEdit.setText(self.entrada)

    def valor_pow(self):
        try:
            self.entrada = self.lineEdit.text()
            self.entrada += '*' + self.entrada
            self.entrada = str(round(eval(self.entrada), 6))
            self.lineEdit.setText(self.entrada)
        except:
            self.lineEdit.clear()
            self.statusbar.showMessage("Error, Operacion invalida")

    def clear(self):
        self.lineEdit.clear()
        self.statusbar.showMessage("")

    def back(self):
        self.entrada = self.lineEdit.text()
        self.entrada = self.entrada[:-1]
        self.lineEdit.setText(self.entrada)

    def eq(self):
        try:
            self.entrada = self.lineEdit.text()
            self.entrada = str(round(eval(self.entrada), 5))
            self.lineEdit.setText(self.entrada)
        except:
            self.lineEdit.clear()
            self.statusbar.showMessage("Error, Operacion invalida")

    def ayuda(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Ayuda')
        msg.setText("Estas es una calculadora de operaciones basica.")
        msg.setDetailedText("Mientras las operaciones sean validas se obtendran resultados, "
                            "en caso contrario, no se podra ejecutar la operacion y la pantalla"
                            " se limpiara automaticamente.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def acerdaDe(self):
        msg = QMessageBox()
        msg.setWindowTitle("Acerca de")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Desarrollado por Antonio Mejia")
        msg.setInformativeText("SEANT")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
