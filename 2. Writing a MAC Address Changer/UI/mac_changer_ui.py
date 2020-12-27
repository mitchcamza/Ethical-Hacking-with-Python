# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mac_changer.ui'
#
# Created: Sun Mar 22 18:31:09 2020
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_mac_changer(object):
    def setupUi(self, mac_changer):
        mac_changer.setObjectName(_fromUtf8("mac_changer"))
        mac_changer.resize(151, 144)
        self.verticalLayout = QtGui.QVBoxLayout(mac_changer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.combobox_interface = QtGui.QComboBox(mac_changer)
        self.combobox_interface.setObjectName(_fromUtf8("combobox_interface"))
        self.combobox_interface.addItem(_fromUtf8(""))
        self.combobox_interface.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.combobox_interface)
        self.new_mac = QtGui.QLineEdit(mac_changer)
        self.new_mac.setObjectName(_fromUtf8("new_mac"))
        self.verticalLayout.addWidget(self.new_mac)
        self.random = QtGui.QPushButton(mac_changer)
        self.random.setObjectName(_fromUtf8("random"))
        self.verticalLayout.addWidget(self.random)
        self.change_mac = QtGui.QPushButton(mac_changer)
        self.change_mac.setObjectName(_fromUtf8("change_mac"))
        self.verticalLayout.addWidget(self.change_mac)

        self.retranslateUi(mac_changer)
        QtCore.QMetaObject.connectSlotsByName(mac_changer)

    def retranslateUi(self, mac_changer):
        mac_changer.setWindowTitle(_translate("mac_changer", "Mac Changer", None))
        self.combobox_interface.setItemText(0, _translate("mac_changer", "eth0", None))
        self.combobox_interface.setItemText(1, _translate("mac_changer", "wlan0", None))
        self.new_mac.setPlaceholderText(_translate("mac_changer", "New MAC", None))
        self.random.setText(_translate("mac_changer", "Generate Random", None))
        self.change_mac.setText(_translate("mac_changer", "Change MAC", None))

