# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectables.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Selectables(object):
    def setupUi(self, Selectables):
        Selectables.setObjectName("Selectables")
        Selectables.resize(466, 287)
        self.centralwidget = QtWidgets.QWidget(Selectables)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 30, 50, 20))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 50, 107, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 70, 76, 20))
        self.radioButton.setObjectName("radioButton")
        self.rb_none = QtWidgets.QRadioButton(self.groupBox)
        self.rb_none.setGeometry(QtCore.QRect(10, 90, 100, 20))
        self.rb_none.setChecked(True)
        self.rb_none.setObjectName("rb_none")
        self.horizontalLayout.addWidget(self.groupBox)
        self.cb_extra_shot = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_extra_shot.setObjectName("cb_extra_shot")
        self.horizontalLayout.addWidget(self.cb_extra_shot)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        Selectables.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Selectables)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 22))
        self.menubar.setObjectName("menubar")
        Selectables.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Selectables)
        self.statusbar.setObjectName("statusbar")
        Selectables.setStatusBar(self.statusbar)

        self.retranslateUi(Selectables)
        QtCore.QMetaObject.connectSlotsByName(Selectables)

    def retranslateUi(self, Selectables):
        _translate = QtCore.QCoreApplication.translate
        Selectables.setWindowTitle(_translate("Selectables", "Selectable Buttons"))
        self.groupBox.setTitle(_translate("Selectables", "Milk"))
        self.radioButton_2.setText(_translate("Selectables", "2%"))
        self.radioButton_3.setText(_translate("Selectables", "Half-and-half"))
        self.radioButton.setText(_translate("Selectables", "Soy Milk"))
        self.rb_none.setText(_translate("Selectables", "None"))
        self.cb_extra_shot.setText(_translate("Selectables", "Extra shot"))
        self.checkBox.setToolTip(_translate("Selectables", "Check to add sugar"))
        self.checkBox.setText(_translate("Selectables", "Sugar"))

