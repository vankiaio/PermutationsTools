# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\fanghan\Hello\hellodialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 341)
        Dialog.setSizeGripEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 501, 91))
        self.groupBox.setObjectName("groupBox")
        self.txtSourcePath = QtWidgets.QTextEdit(self.groupBox)
        self.txtSourcePath.setGeometry(QtCore.QRect(30, 20, 411, 61))
        self.txtSourcePath.setObjectName("txtSourcePath")
        self.pbtn_browsepath = QtWidgets.QPushButton(self.groupBox)
        self.pbtn_browsepath.setGeometry(QtCore.QRect(450, 20, 31, 28))
        self.pbtn_browsepath.setObjectName("pbtn_browsepath")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 140, 501, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtDestionPath = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtDestionPath.setGeometry(QtCore.QRect(30, 20, 411, 61))
        self.txtDestionPath.setObjectName("txtDestionPath")
        self.pbtn_browsepath_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pbtn_browsepath_2.setGeometry(QtCore.QRect(450, 20, 31, 28))
        self.pbtn_browsepath_2.setObjectName("pbtn_browsepath_2")
        self.pbtn_generate = QtWidgets.QPushButton(Dialog)
        self.pbtn_generate.setGeometry(QtCore.QRect(100, 260, 93, 28))
        self.pbtn_generate.setObjectName("pbtn_generate")
        self.pbtn_close = QtWidgets.QPushButton(Dialog)
        self.pbtn_close.setGeometry(QtCore.QRect(280, 260, 93, 28))
        self.pbtn_close.setObjectName("pbtn_close")

        self.retranslateUi(Dialog)
        self.pbtn_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "数据源路径"))
        self.pbtn_browsepath.setText(_translate("Dialog", "..."))
        self.groupBox_2.setTitle(_translate("Dialog", "生成文本路径"))
        self.pbtn_browsepath_2.setText(_translate("Dialog", "..."))
        self.pbtn_generate.setText(_translate("Dialog", "生成"))
        self.pbtn_close.setText(_translate("Dialog", "关闭"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

