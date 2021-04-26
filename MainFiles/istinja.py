# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from project import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 620)
        MainWindow.setMinimumSize(QtCore.QSize(900, 620))
        MainWindow.setMaximumSize(QtCore.QSize(900, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, -40, 901, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.MainHeadingLabel = QtWidgets.QLabel(self.MainTab)
        self.MainHeadingLabel.setGeometry(QtCore.QRect(160, 20, 571, 141))
        self.MainHeadingLabel.setObjectName("MainHeadingLabel")
        self.Chapter2label = QtWidgets.QLabel(self.MainTab)
        self.Chapter2label.setGeometry(QtCore.QRect(120, 230, 231, 211))
        self.Chapter2label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Chapter2label.setObjectName("Chapter2label")
        self.Chapter3label = QtWidgets.QLabel(self.MainTab)
        self.Chapter3label.setGeometry(QtCore.QRect(530, 230, 261, 211))
        self.Chapter3label.setObjectName("Chapter3label")
        self.Chapter2Button = QtWidgets.QPushButton(self.MainTab)
        self.Chapter2Button.setGeometry(QtCore.QRect(160, 480, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chapter2Button.setFont(font)
        self.Chapter2Button.setMouseTracking(False)
        self.Chapter2Button.setObjectName("Chapter2Button")
        self.Chapter3Button = QtWidgets.QPushButton(self.MainTab)
        self.Chapter3Button.setGeometry(QtCore.QRect(580, 480, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chapter3Button.setFont(font)
        self.Chapter3Button.setMouseTracking(False)
        self.Chapter3Button.setObjectName("Chapter3Button")
        self.tabWidget.addTab(self.MainTab, "")
        self.Chapter2Tab = QtWidgets.QWidget()
        self.Chapter2Tab.setObjectName("Chapter2Tab")
        self.Chapter2Heading = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chapter2Heading.setGeometry(QtCore.QRect(100, 30, 731, 101))
        self.Chapter2Heading.setObjectName("Chapter2Heading")
        self.Chp2choicebox = QtWidgets.QComboBox(self.Chapter2Tab)
        self.Chp2choicebox.setGeometry(QtCore.QRect(330, 180, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chp2choicebox.setFont(font)
        self.Chp2choicebox.setObjectName("Chp2choicebox")
        self.Chp2choicebox.addItem("")
        self.Chp2choicebox.addItem("")
        self.Chp2choicebox.addItem("")
        self.Chp2choicebox.addItem("")
        self.Chp2choicebox.addItem("")
        self.Chp2label = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chp2label.setGeometry(QtCore.QRect(20, 150, 551, 31))
        self.Chp2label.setObjectName("Chp2label")
        self.Chp2funclabel = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chp2funclabel.setGeometry(QtCore.QRect(20, 210, 551, 31))
        self.Chp2funclabel.setObjectName("Chp2funclabel")
        self.Chp2FuncInput = QtWidgets.QLineEdit(self.Chapter2Tab)
        self.Chp2FuncInput.setGeometry(QtCore.QRect(330, 250, 271, 31))
        self.Chp2FuncInput.setObjectName("Chp2FuncInput")
        self.Chp2Ainput = QtWidgets.QLineEdit(self.Chapter2Tab)
        self.Chp2Ainput.setGeometry(QtCore.QRect(290, 330, 113, 31))
        self.Chp2Ainput.setInputMask("")
        self.Chp2Ainput.setMaxLength(32767)
        self.Chp2Ainput.setObjectName("Chp2Ainput")
        self.Chp2Binput = QtWidgets.QLineEdit(self.Chapter2Tab)
        self.Chp2Binput.setGeometry(QtCore.QRect(510, 330, 113, 31))
        self.Chp2Binput.setInputMask("")
        self.Chp2Binput.setMaxLength(32767)
        self.Chp2Binput.setObjectName("Chp2Binput")
        self.Chp2formulalabel = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chp2formulalabel.setGeometry(QtCore.QRect(30, 450, 611, 111))
        self.Chp2formulalabel.setObjectName("Chp2formulalabel")
        self.Chp2startbutton = QtWidgets.QPushButton(self.Chapter2Tab)
        self.Chp2startbutton.setGeometry(QtCore.QRect(700, 480, 171, 71))
        self.Chp2startbutton.setObjectName("Chp2startbutton")
        self.Chp2tolinput = QtWidgets.QLineEdit(self.Chapter2Tab)
        self.Chp2tolinput.setGeometry(QtCore.QRect(390, 400, 113, 31))
        self.Chp2tolinput.setInputMask("")
        self.Chp2tolinput.setMaxLength(32767)
        self.Chp2tolinput.setObjectName("Chp2tolinput")
        self.Chp2mainback = QtWidgets.QPushButton(self.Chapter2Tab)
        self.Chp2mainback.setGeometry(QtCore.QRect(720, 390, 141, 71))
        self.Chp2mainback.setObjectName("Chp2mainback")
        self.Chp2pointslabel = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chp2pointslabel.setGeometry(QtCore.QRect(20, 290, 551, 31))
        self.Chp2pointslabel.setObjectName("Chp2pointslabel")
        self.Chp2toleranclabel = QtWidgets.QLabel(self.Chapter2Tab)
        self.Chp2toleranclabel.setGeometry(QtCore.QRect(20, 370, 551, 31))
        self.Chp2toleranclabel.setObjectName("Chp2toleranclabel")
        self.tabWidget.addTab(self.Chapter2Tab, "")
        self.Chapter2iterTab = QtWidgets.QWidget()
        self.Chapter2iterTab.setObjectName("Chapter2iterTab")
        self.Chp2Itertablabel = QtWidgets.QLabel(self.Chapter2iterTab)
        self.Chp2Itertablabel.setGeometry(QtCore.QRect(190, 10, 521, 91))
        self.Chp2Itertablabel.setObjectName("Chp2Itertablabel")
        self.Chp2Table = QtWidgets.QTableWidget(self.Chapter2iterTab)
        self.Chp2Table.setGeometry(QtCore.QRect(60, 130, 771, 361))
        self.Chp2Table.setRowCount(0)
        self.Chp2Table.setColumnCount(6)
        self.Chp2Table.setObjectName("Chp2Table")
        self.Chp2Table.horizontalHeader().setVisible(False)
        self.Chp2Table.horizontalHeader().setDefaultSectionSize(128)
        self.Chp2Table.horizontalHeader().setSortIndicatorShown(False)
        self.Chp2Table.horizontalHeader().setStretchLastSection(False)
        self.Chp2Table.verticalHeader().setVisible(False)
        self.Chp2Table.verticalHeader().setCascadingSectionResizes(False)
        self.Chp2Anslabel = QtWidgets.QLabel(self.Chapter2iterTab)
        self.Chp2Anslabel.setGeometry(QtCore.QRect(160, 510, 461, 61))
        self.Chp2Anslabel.setObjectName("Chp2Anslabel")
        self.Chp2iterback = QtWidgets.QPushButton(self.Chapter2iterTab)
        self.Chp2iterback.setGeometry(QtCore.QRect(670, 510, 141, 71))
        self.Chp2iterback.setObjectName("Chp2iterback")
        self.tabWidget.addTab(self.Chapter2iterTab, "")
        self.Chapter3Tab = QtWidgets.QWidget()
        self.Chapter3Tab.setObjectName("Chapter3Tab")
        self.Chapter3Heading = QtWidgets.QLabel(self.Chapter3Tab)
        self.Chapter3Heading.setGeometry(QtCore.QRect(190, 0, 461, 91))
        self.Chapter3Heading.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Chapter3Heading.setFont(font)
        self.Chapter3Heading.setTextFormat(QtCore.Qt.RichText)
        self.Chapter3Heading.setAlignment(QtCore.Qt.AlignCenter)
        self.Chapter3Heading.setWordWrap(False)
        self.Chapter3Heading.setObjectName("Chapter3Heading")
        self.Ch3FormulaLabel = QtWidgets.QLabel(self.Chapter3Tab)
        self.Ch3FormulaLabel.setGeometry(QtCore.QRect(10, 90, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Ch3FormulaLabel.setFont(font)
        self.Ch3FormulaLabel.setObjectName("Ch3FormulaLabel")
        self.Ch3choicebox = QtWidgets.QComboBox(self.Chapter3Tab)
        self.Ch3choicebox.setGeometry(QtCore.QRect(470, 120, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ch3choicebox.setFont(font)
        self.Ch3choicebox.setMaxVisibleItems(5)
        self.Ch3choicebox.setObjectName("Ch3choicebox")
        self.Ch3choicebox.addItem("")
        self.Ch3choicebox.addItem("")
        self.Ch3choicebox.addItem("")
        self.Ch3choicebox.addItem("")
        self.Ch3choicebox.addItem("")
        self.Ch3choicebox.addItem("")
        self.Ch3XValLabel = QtWidgets.QLabel(self.Chapter3Tab)
        self.Ch3XValLabel.setGeometry(QtCore.QRect(10, 160, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Ch3XValLabel.setFont(font)
        self.Ch3XValLabel.setObjectName("Ch3XValLabel")
        self.x0 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x0.setGeometry(QtCore.QRect(20, 210, 113, 20))
        self.x0.setObjectName("x0")
        self.x1 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x1.setGeometry(QtCore.QRect(150, 210, 113, 20))
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x2.setGeometry(QtCore.QRect(280, 210, 113, 20))
        self.x2.setObjectName("x2")
        self.x3 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x3.setGeometry(QtCore.QRect(410, 210, 113, 20))
        self.x3.setObjectName("x3")
        self.x4 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x4.setGeometry(QtCore.QRect(540, 210, 113, 20))
        self.x4.setObjectName("x4")
        self.x5 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.x5.setGeometry(QtCore.QRect(670, 210, 113, 20))
        self.x5.setObjectName("x5")
        self.Ch3YValLabel = QtWidgets.QLabel(self.Chapter3Tab)
        self.Ch3YValLabel.setGeometry(QtCore.QRect(10, 250, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Ch3YValLabel.setFont(font)
        self.Ch3YValLabel.setObjectName("Ch3YValLabel")
        self.y0 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y0.setGeometry(QtCore.QRect(20, 290, 113, 20))
        self.y0.setObjectName("y0")
        self.y1 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y1.setGeometry(QtCore.QRect(150, 290, 113, 20))
        self.y1.setObjectName("y1")
        self.y2 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y2.setGeometry(QtCore.QRect(280, 290, 113, 20))
        self.y2.setObjectName("y2")
        self.y3 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y3.setGeometry(QtCore.QRect(410, 290, 113, 20))
        self.y3.setObjectName("y3")
        self.y4 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y4.setGeometry(QtCore.QRect(540, 290, 113, 20))
        self.y4.setObjectName("y4")
        self.y5 = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.y5.setGeometry(QtCore.QRect(670, 290, 113, 20))
        self.y5.setObjectName("y5")
        self.Ch3InterpolLabel = QtWidgets.QLabel(self.Chapter3Tab)
        self.Ch3InterpolLabel.setGeometry(QtCore.QRect(10, 330, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Ch3InterpolLabel.setFont(font)
        self.Ch3InterpolLabel.setObjectName("Ch3InterpolLabel")
        self.InterPolVal = QtWidgets.QLineEdit(self.Chapter3Tab)
        self.InterPolVal.setGeometry(QtCore.QRect(320, 330, 113, 20))
        self.InterPolVal.setObjectName("InterPolVal")
        self.StartInterpolationButton = QtWidgets.QPushButton(self.Chapter3Tab)
        self.StartInterpolationButton.setGeometry(QtCore.QRect(650, 410, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.StartInterpolationButton.setFont(font)
        self.StartInterpolationButton.setObjectName("StartInterpolationButton")
        self.MainMenuButton = QtWidgets.QPushButton(self.Chapter3Tab)
        self.MainMenuButton.setGeometry(QtCore.QRect(50, 412, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.MainMenuButton.setFont(font)
        self.MainMenuButton.setObjectName("MainMenuButton")
        self.tabWidget.addTab(self.Chapter3Tab, "")
        self.InterpolationTab = QtWidgets.QWidget()
        self.InterpolationTab.setObjectName("InterpolationTab")
        self.InterPolHeadinglabel = QtWidgets.QLabel(self.InterpolationTab)
        self.InterPolHeadinglabel.setGeometry(QtCore.QRect(270, 20, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.InterPolHeadinglabel.setFont(font)
        self.InterPolHeadinglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InterPolHeadinglabel.setObjectName("InterPolHeadinglabel")
        self.DifferenceTable = QtWidgets.QTableWidget(self.InterpolationTab)
        self.DifferenceTable.setGeometry(QtCore.QRect(40, 80, 811, 271))
        self.DifferenceTable.setObjectName("DifferenceTable")
        self.DifferenceTable.setColumnCount(0)
        self.DifferenceTable.setRowCount(0)
        self.InterpolAnsLabel = QtWidgets.QLabel(self.InterpolationTab)
        self.InterpolAnsLabel.setGeometry(QtCore.QRect(40, 375, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.InterpolAnsLabel.setFont(font)
        self.InterpolAnsLabel.setObjectName("InterpolAnsLabel")
        self.InterPolMainMenu = QtWidgets.QPushButton(self.InterpolationTab)
        self.InterPolMainMenu.setGeometry(QtCore.QRect(630, 490, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.InterPolMainMenu.setFont(font)
        self.InterPolMainMenu.setObjectName("InterPolMainMenu")
        self.tabWidget.addTab(self.InterpolationTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Ch3choicebox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Computing and Analysis Software"))
        self.MainHeadingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">Numerical Computing</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">and Analysis Software</span></p></body></html>"))
        self.Chapter2label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Solutions of Equations </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">in one Variable</span></p><p><span style=\" font-size:12pt;\">1 ) Bisection Method</span></p><p><span style=\" font-size:12pt;\">2 ) Regulai Falsi Method</span></p><p><span style=\" font-size:12pt;\">3 ) Newton - Raphson Method</span></p><p><span style=\" font-size:12pt;\">4 ) Secant Method</span></p><p><span style=\" font-size:12pt;\">5 ) Fixed Point Iteration</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.Chapter3label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Interpolation and </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Polynomial Approximation</span></p><p><span style=\" font-size:11pt;\">1 ) Lagrange Polynomial</span></p><p><span style=\" font-size:11pt;\">2) Newton Divided Difference</span></p><p><span style=\" font-size:11pt;\">3) Newton Foward Backwards (DDT)</span></p><p><span style=\" font-size:11pt;\">4 ) Newton Forward Backwards (SDT)</span></p><p><span style=\" font-size:11pt;\">5 ) Stirling\'s Method</span></p></body></html>"))
        self.Chapter2Button.setText(_translate("MainWindow", "Click here \n"
" for Chapter 2"))
        self.Chapter3Button.setText(_translate("MainWindow", "Click here \n"
" for Chapter 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), _translate("MainWindow", "Tab 1"))
        self.Chapter2Heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">Solutions of Equations </span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">in one Variable</span></p></body></html>"))
        self.Chp2choicebox.setItemText(0, _translate("MainWindow", "Bisection Method"))
        self.Chp2choicebox.setItemText(1, _translate("MainWindow", "Regulai Falsi Method"))
        self.Chp2choicebox.setItemText(2, _translate("MainWindow", "Newton - Raphson Method"))
        self.Chp2choicebox.setItemText(3, _translate("MainWindow", "Secant Method"))
        self.Chp2choicebox.setItemText(4, _translate("MainWindow", "Fixed Point Iteration Method"))
        self.Chp2label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Choose Your Method for Finding the root of the equation below:</span></p></body></html>"))
        self.Chp2funclabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Input your equation f(x) below:</span></p></body></html>"))
        self.Chp2FuncInput.setText(_translate("MainWindow", "Example: 2x - 5x^2 = 0"))
        self.Chp2Ainput.setText(_translate("MainWindow", "Ex: 2.6897"))
        self.Chp2Binput.setText(_translate("MainWindow", "Ex: 2.6897"))
        self.Chp2formulalabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Bisection Method Formula:</span></p><p align=\"center\">Root: c = (a+b)/2</p></body></html>"))
        self.Chp2startbutton.setText(_translate("MainWindow", "Click Here to \n"
" Start the Interpolation"))
        self.Chp2tolinput.setText(_translate("MainWindow", "Ex: 0.000001"))
        self.Chp2mainback.setText(_translate("MainWindow", "Back to \n"
" Main Menu"))
        self.Chp2pointslabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Input the initial points a and b below:</span></p></body></html>"))
        self.Chp2toleranclabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Input the Tolerance Value below:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Chapter2Tab), _translate("MainWindow", "Page"))
        self.Chp2Itertablabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Performed Iterations for</span></p><p align=\"center\"><span style=\" font-size:24pt;\"> *insert function here*</span></p></body></html>"))
        self.Chp2Anslabel.setText(_translate("MainWindow", "TextLabel"))
        self.Chp2iterback.setText(_translate("MainWindow", "Back to \n"
" Chapter 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Chapter2iterTab), _translate("MainWindow", "Page"))
        self.Chapter3Heading.setText(_translate("MainWindow", "INTERPOLATION "))
        self.Ch3FormulaLabel.setText(_translate("MainWindow", "Select the required Interpolation formula from the combo box :"))
        self.Ch3choicebox.setCurrentText(_translate("MainWindow", "Lagrange Interpolation"))
        self.Ch3choicebox.setItemText(0, _translate("MainWindow", "Lagrange Interpolation"))
        self.Ch3choicebox.setItemText(1, _translate("MainWindow", "Forwards-SDT"))
        self.Ch3choicebox.setItemText(2, _translate("MainWindow", "Backwards-SDT"))
        self.Ch3choicebox.setItemText(3, _translate("MainWindow", "Forwards-DDT"))
        self.Ch3choicebox.setItemText(4, _translate("MainWindow", "Backwards-DDT"))
        self.Ch3choicebox.setItemText(5, _translate("MainWindow", "Stirling Central Difference"))
        self.Ch3XValLabel.setText(_translate("MainWindow", "Enter the x values here (enter 0 where not required) :"))
        self.x0.setText(_translate("MainWindow", "0"))
        self.x1.setText(_translate("MainWindow", "0"))
        self.x2.setText(_translate("MainWindow", "0"))
        self.x3.setText(_translate("MainWindow", "0"))
        self.x4.setText(_translate("MainWindow", "0"))
        self.x5.setText(_translate("MainWindow", "0"))
        self.Ch3YValLabel.setText(_translate("MainWindow", "Enter the y values here (enter 0 where not required) :"))
        self.y0.setText(_translate("MainWindow", "0"))
        self.y1.setText(_translate("MainWindow", "0"))
        self.y2.setText(_translate("MainWindow", "0"))
        self.y3.setText(_translate("MainWindow", "0"))
        self.y4.setText(_translate("MainWindow", "0"))
        self.y5.setText(_translate("MainWindow", "0"))
        self.Ch3InterpolLabel.setText(_translate("MainWindow", "Enter the value to interpolate:"))
        self.InterPolVal.setText(_translate("MainWindow", "0"))
        self.StartInterpolationButton.setText(_translate("MainWindow", "Start Interpolation"))
        self.MainMenuButton.setText(_translate("MainWindow", "Back To Main Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Chapter3Tab), _translate("MainWindow", "Page"))
        self.InterPolHeadinglabel.setText(_translate("MainWindow", "DIFFERENCE TABLE"))
        self.InterpolAnsLabel.setText(_translate("MainWindow", "The Interpolated value is :"))
        self.InterPolMainMenu.setText(_translate("MainWindow", "Back To Main Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InterpolationTab), _translate("MainWindow", "Page"))

    def MovetoChapter2(self, MainWindow):
        self.Chp2Table.setColumnCount(6)
        self.Chp2Table.setHorizontalHeaderLabels(["Iteration","a","b","c","f(c)","Error"])
        self.tabWidget.setCurrentIndex(1)
    def Chp2ChoiceChanged(self, MainWindow):
        method = self.Chp2choicebox.currentText()
        if(method=="Bisection Method"):
            self.Chp2formulalabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Bisection Method Formula:</span></p><p align=\"center\">Root: c = (a+b)/2</p></body></html>")
        elif(method=="Regulai Falsi Method"):
            self.Chp2formulalabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Regulai Falsi Method Formula:</span></p><p align=\"center\">Root: c = af(b) - bf(a) / f(b) - f(a)</p></body></html>")
        elif(method=="Newton - Raphson Method"):
            self.Chp2formulalabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Newton - Raphson Method Formula:</span></p><p align=\"center\">Root: P = P<sub>n-1</sub> - f(P<sub>n-1</sub>) / f`(P<sub>n-1</sub>)</p></body></html>")
        elif(method=="Secant Method"):
            self.Chp2formulalabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Secant Method Formula:</span></p><p align=\"center\">Root: x<sub>n+1</sub> = x<sub>n-1</sub>f(x<sub>n</sub>) - x<sub>n</sub>f(x<sub>n-1</sub>) / f(x<sub>n</sub>) - f(x<sub>n-1</sub>) </p></body></html>")
        elif(method=="Fixed Point Iteration Method"):
            self.Chp2funclabel.setText("<html><b>Input your equation G(x) below:</b></html>")
            self.Chp2formulalabel.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Fixed Point Iteration Method Formula:</span></p><p align=\"center\">The Root will be based on the equation input by you!</p></body></html>")

    def MovetoMain(self, MainWindow):
        self.tabWidget.setCurrentIndex(0)
    def Chapter2Start(self, Mainwindow):
        self.Chp2Table.horizontalHeader().setVisible(True)
        try:
            equation = self.Chp2FuncInput.text()
            Newstr = MakeStringReady(equation)
            Newstr = sympify(Newstr)
            Mainvar = FindMainVar(equation)
            Newvar = symbols(Mainvar)
            a = float(self.Chp2Ainput.text())
            b = float(self.Chp2Binput.text())
            tolerance = float(self.Chp2tolinput.text())
        except:
            dialoguebox = QMessageBox(QMessageBox.Critical, "Error", "Please provide Valid Input. The equation must be Single Variable and the other inputs must be proper numerical values")
            x=dialoguebox.exec_()
            return
        self.tabWidget.setCurrentIndex(2)
        self.Chp2Itertablabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Performed Iterations for</span></p><p align=\"center\"><span style=\" font-size:24pt;\"> {equation}</span></p></body></html>")
        method=str(self.Chp2choicebox.currentText())
        self.Chp2Table.setHorizontalHeaderLabels(["Iteration","a","b","c","f(c)","Error"])
        if(method=="Bisection Method"):
            Ans=Bisection(Newstr, Newvar, a, b, tolerance, self.Chp2Table)
            self.Chp2Anslabel.setText("The Root of the equation " + str(equation) + " is: " + str(Ans))
            if(Ans=="None"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The Entry points provided Failed the Intermediate Value Theorum")
                x=dialoguebox.exec_()
                return
        elif(method=="Regulai Falsi Method"):
            Ans=RegularFalsi(Newstr, Newvar, a, b, tolerance, self.Chp2Table)
            self.Chp2Anslabel.setText("The Root of the equation " + str(equation) + " is: " + str(Ans))
            if(Ans=="None"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The Entry points provided Failed the Intermediate Value Theorum")
                x=dialoguebox.exec_()
                return
        elif(method=="Newton - Raphson Method"):
            self.Chp2Table.setColumnCount(5)
            self.Chp2Table.setHorizontalHeaderLabels(["Iteration","a","c","f(c)","Error"])
            self.Chp2Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            Ans=NewtonRaphson(Newstr, Newvar, a, b, tolerance, self.Chp2Table)
            self.Chp2Anslabel.setText("The Root of the equation " + str(equation) + " is: " + str(Ans))
        elif(method=="Secant Method"):
            Ans=Secant(Newstr, Newvar, a, b, tolerance, self.Chp2Table)
            self.Chp2Anslabel.setText("The Root of the equation " + str(equation) + " is: " + str(Ans))
        elif(method=="Fixed Point Iteration Method"):
            self.Chp2Table.setColumnCount(4)
            self.Chp2Table.setHorizontalHeaderLabels(["Iteration","x","f(x)","Error"])
            self.Chp2Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            Ans=FixedPointIteration(Newstr, Newvar, a, b, tolerance, self.Chp2Table)
            self.Chp2Anslabel.setText("The Root of the equation " + str(equation) + " is: " + str(Ans))
            if(Ans=="Complex"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The function provided returns a complex value!")
                x=dialoguebox.exec_()
                return
            elif(Ans=="Bouncing"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The function provided bounces between two values!")
                x=dialoguebox.exec_()
                return
            elif(Ans=="Divergent"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The function provided is a divergent function!")
                x=dialoguebox.exec_()
                return
            elif(Ans=="200 iterations"):
                dialoguebox = QMessageBox(QMessageBox.Warning, "Error", "The function provided did not reach the tolerance value even after 200 iterations! Execution terminated to save resources.")
                x=dialoguebox.exec_()
                return
    def MovetoChapter3(self,MainWindow):
            self.tabWidget.setCurrentIndex(3)
            return

    def Chapter3Start(self,MainWindow):
        self.DifferenceTable.setColumnCount(6)
        self.tabWidget.setCurrentIndex(3)
        try:
                x=np.zeros(6,dtype=float)
                InterPolVal=float(self.InterPolVal.text())
                y=np.zeros(6,dtype=float)
                x[0]=float((self.x0.text()))
                x[1]=float((self.x1.text()))
                x[2]=float((self.x2.text()))
                x[3]=float((self.x3.text()))
                x[4]=float((self.x4.text()))
                x[5]=float((self.x5.text()))
                y[0]=float((self.y0.text()))
                y[1]=float((self.y1.text()))
                y[2]=float((self.y2.text()))
                y[3]=float((self.y3.text()))
                y[4]=float((self.y4.text()))
                y[5]=float((self.y5.text()))
        except:
                dialoguebox = QMessageBox(QMessageBox.Critical, "Error", "Please provide Valid Input.")
                x=dialoguebox.exec_()
                return
        method= str(self.Ch3choicebox.currentText())
        if method=="Stirling Central Difference":
                Ans=StirlingsMethod(InterPolVal,5,x,y,self.DifferenceTable)
                self.tabWidget.setCurrentIndex(4)
                self.InterpolAnsLabel.setText("The Interpolated value is = "+ str(Ans))
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.Chapter2Button.clicked.connect(lambda: ui.MovetoChapter2(MainWindow))
    ui.Chp2startbutton.clicked.connect(lambda: ui.Chapter2Start(MainWindow))
    ui.Chp2mainback.clicked.connect(lambda: ui.MovetoMain(MainWindow))
    ui.Chp2iterback.clicked.connect(lambda: ui.MovetoChapter2(MainWindow))
    ui.Chp2choicebox.currentIndexChanged.connect(lambda: ui.Chp2ChoiceChanged(MainWindow))
    ui.Chapter3Button.clicked.connect(lambda: ui.MovetoChapter3(MainWindow))
    ui.StartInterpolationButton.clicked.connect(lambda: ui.Chapter3Start(MainWindow))
    sys.exit(app.exec_())

