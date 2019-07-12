# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import QDir
from Ui_hellodialog import Ui_Dialog
import numpy as np
import pandas as pd
import itertools as its

class HelloDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HelloDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pbtn_browsepath_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.getText()
    
    @pyqtSlot()
    def on_pbtn_generate_clicked(self):
        """
        Slot documentation goes here.
        """
        
        arrSC = ['∈',  '∉', '∊', '∋', '∌', '∍', '∎', '∏', '∐', '∑', '∓', '∔', '∗', '∘', '√', '∝', '∞', '∠'
                     '∡', '∢', '∤', '∥', '∦', '∧', '∨', '∩', '∪', '∫', '∬', '∭', '∮', '∯', '∰', '∱', '∲', '∳'
                     '∴', '∵', '∶', '∷', '∸', '∹', '∺', '∻', '∼', '∽', '∾', '∿', '≀', '≁', '≂', '≃', '≄', '≅'
                     '≆', '≇', '≈', '≉', '≊', '≋', '≌', '≍', '≎', '≏', '≐', '≑', '≒', '≓', '≔', '≕', '≖', '≗'
                     '≘', '≙', '≚', '≛', '≜', '≟', '≠', '≡', '≢', '≣', '≤', '≥', '≦', '≧', '≨', '≩', '≪', '≫'
                     '≬', '≭', '≮', '≰', '≱', '≲', '≳', '≴', '≵', '≶', '≷', '≸', '≹', '≺', '≻', '≼', '≽', '≾'
                     '≿', '⊀', '⊁', '⊂', '⊃', '⊄', '⊅', '⊆', '⊇', '⊈', '⊉', '⊊', '⊋', '⊌', '⊍', '⊎', '⊏', '⊐'
                     '⊑', '⊒', '⊓', '⊔', '►', '▽', '◀', '◁', '◆', '◈', '◉', '◍', '◎', '●', '◐', '◑', '◒', '◓'
                     '◔', '◕', '◖', '◗', '◘', '◙', '◚', '◛', '◜', '◝', '◞', '◟', '◠', '◡', '◢', '◣', '◤', '◥'
                     '◦', '◧', '◨', '◩', '◪', '◫', '◬', '◭', '◮', '◯']
        sourcepath = "template.xlsx"
        outputpath = "excel2txt.txt"
        if self.txtSourcePath.toPlainText().strip() != "":
            sourcepath = self.txtSourcePath.toPlainText()
            print(sourcepath)
            
        if self.txtDestionPath.toPlainText().strip() != "":
            outputpath = self.txtDestionPath.toPlainText()
            print(outputpath)
 
        #dfSC= pd.read_excel("specialCharacters.xlsx")
        #arrSC = dfSC.loc[:,['特殊符号']].values.flatten()
        df = pd.read_excel(sourcepath)
        #print(df.dropna(how = 'all',axis=1))
        df2 = pd.DataFrame([r for r in its.product(df.标题, df.内容, df.标签, df.地区, df.联系方式, df.超链接文本)], columns=df.columns)
        df_new = df2.dropna().reset_index(drop=True) 
        #print(df_new)
        df_new.insert(5, "randSpecCharacterCol", np.random.choice(arrSC, df_new.shape[0]), True) 
        df1column = df_new.astype(str).sum(1)
        df1column.to_csv(outputpath, sep=',', index=False)
        #print(df1column)
        
    @pyqtSlot()
    def on_pbtn_browsepath_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.getText2()
        
    def getText(self):
         dialog=QFileDialog()
         dialog.setFileMode(QFileDialog.AnyFile)#可选任意文件
         dialog.setFilter(QDir.Files)
 
         if dialog.exec_():#该方法用于选择文件，如果选中文件则返回true
             filenames=dialog.selectedFiles()#获取选中文件名列表
             print(filenames)
             f=open(filenames[0],'r')
             with f:
                 self.txtSourcePath.setPlainText(filenames[0])
                 print(filenames)
                 #data=f.read()
                 #self.contents.setText(filenames) 
                 
    def getText2(self):
         dialog=QFileDialog()
         dialog.setFileMode(QFileDialog.AnyFile)#可选任意文件
         dialog.setFilter(QDir.Files)
 
         if dialog.exec_():#该方法用于选择文件，如果选中文件则返回true
            filenames=dialog.selectedFiles()#获取选中文件名列表
            print(filenames)
            self.txtDestionPath.setPlainText(filenames[0])
             
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dlg = HelloDialog()
    dlg.show()
    sys.exit(app.exec_())
    
