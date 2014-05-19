# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Mon May 19 13:05:35 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(499, 239)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtInputCellFile = QtGui.QLineEdit(self.centralwidget)
        self.txtInputCellFile.setGeometry(QtCore.QRect(130, 50, 331, 20))
        self.txtInputCellFile.setObjectName(_fromUtf8("txtInputCellFile"))
        self.txtInputNeighborFile = QtGui.QLineEdit(self.centralwidget)
        self.txtInputNeighborFile.setGeometry(QtCore.QRect(130, 80, 331, 20))
        self.txtInputNeighborFile.setObjectName(_fromUtf8("txtInputNeighborFile"))
        self.btnGenerateCellFile = QtGui.QPushButton(self.centralwidget)
        self.btnGenerateCellFile.setGeometry(QtCore.QRect(320, 120, 161, 41))
        self.btnGenerateCellFile.setObjectName(_fromUtf8("btnGenerateCellFile"))
        self.btnInputCellFile = QtGui.QPushButton(self.centralwidget)
        self.btnInputCellFile.setGeometry(QtCore.QRect(460, 50, 21, 21))
        self.btnInputCellFile.setObjectName(_fromUtf8("btnInputCellFile"))
        self.btnInputNeighborFile = QtGui.QPushButton(self.centralwidget)
        self.btnInputNeighborFile.setGeometry(QtCore.QRect(460, 80, 21, 21))
        self.btnInputNeighborFile.setObjectName(_fromUtf8("btnInputNeighborFile"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 180, 151, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mnuAbout = QtGui.QMenu(self.menubar)
        self.mnuAbout.setObjectName(_fromUtf8("mnuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCellDatabaseFileFormat = QtGui.QAction(MainWindow)
        self.actionCellDatabaseFileFormat.setObjectName(_fromUtf8("actionCellDatabaseFileFormat"))
        self.actionNeighborFileFormat = QtGui.QAction(MainWindow)
        self.actionNeighborFileFormat.setObjectName(_fromUtf8("actionNeighborFileFormat"))
        self.mnuAbout.addAction(self.actionCellDatabaseFileFormat)
        self.mnuAbout.addAction(self.actionNeighborFileFormat)
        self.mnuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.mnuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtInputCellFile, self.btnInputCellFile)
        MainWindow.setTabOrder(self.btnInputCellFile, self.txtInputNeighborFile)
        MainWindow.setTabOrder(self.txtInputNeighborFile, self.btnInputNeighborFile)
        MainWindow.setTabOrder(self.btnInputNeighborFile, self.btnGenerateCellFile)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Cell Database File", None))
        self.label_2.setText(_translate("MainWindow", "Neighbor File", None))
        self.btnGenerateCellFile.setText(_translate("MainWindow", "Generate Cell File", None))
        self.btnInputCellFile.setText(_translate("MainWindow", "...", None))
        self.btnInputNeighborFile.setText(_translate("MainWindow", "...", None))
        self.label_3.setText(_translate("MainWindow", "TEMS Cell File Generator", None))
        self.label_5.setText(_translate("MainWindow", "Developed by Imtiaz A. Nizami", None))
        self.mnuAbout.setTitle(_translate("MainWindow", "&File", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionCellDatabaseFileFormat.setText(_translate("MainWindow", "CellDatabaseFileFormat", None))
        self.actionNeighborFileFormat.setText(_translate("MainWindow", "NeighborFileFormat", None))

