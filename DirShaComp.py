# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dir_sha_comp.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileReplicants(object):
    def setupUi(self, FileReplicants):
        FileReplicants.setObjectName("FileReplicants")
        FileReplicants.resize(551, 377)
        self.centralwidget = QtWidgets.QWidget(FileReplicants)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.BtnLoadDir = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLoadDir.setObjectName("BtnLoadDir")
        self.gridLayout.addWidget(self.BtnLoadDir, 0, 0, 1, 1)
        self.WorkAreaAnalysisGrp = QtWidgets.QGroupBox(self.centralwidget)
        self.WorkAreaAnalysisGrp.setObjectName("WorkAreaAnalysisGrp")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.WorkAreaAnalysisGrp)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ProcessDebug = QtWidgets.QPlainTextEdit(self.WorkAreaAnalysisGrp)
        self.ProcessDebug.setObjectName("ProcessDebug")
        self.gridLayout_3.addWidget(self.ProcessDebug, 1, 0, 1, 1)
        self.FileList = QtWidgets.QTreeWidget(self.WorkAreaAnalysisGrp)
        self.FileList.setAnimated(True)
        self.FileList.setObjectName("FileList")
        item_0 = QtWidgets.QTreeWidgetItem(self.FileList)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.FileList)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_3.addWidget(self.FileList, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.WorkAreaAnalysisGrp, 1, 1, 6, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.BtnClearDebug = QtWidgets.QPushButton(self.centralwidget)
        self.BtnClearDebug.setObjectName("BtnClearDebug")
        self.gridLayout.addWidget(self.BtnClearDebug, 3, 0, 1, 1)
        self.BtnClearList = QtWidgets.QPushButton(self.centralwidget)
        self.BtnClearList.setObjectName("BtnClearList")
        self.gridLayout.addWidget(self.BtnClearList, 5, 0, 1, 1)
        self.BtnAnalysis = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAnalysis.setObjectName("BtnAnalysis")
        self.gridLayout.addWidget(self.BtnAnalysis, 0, 2, 1, 1)
        self.InputWorkDir = QtWidgets.QLineEdit(self.centralwidget)
        self.InputWorkDir.setObjectName("InputWorkDir")
        self.gridLayout.addWidget(self.InputWorkDir, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        FileReplicants.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FileReplicants)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 22))
        self.menubar.setObjectName("menubar")
        FileReplicants.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FileReplicants)
        self.statusbar.setObjectName("statusbar")
        FileReplicants.setStatusBar(self.statusbar)

        self.retranslateUi(FileReplicants)
        QtCore.QMetaObject.connectSlotsByName(FileReplicants)

    def retranslateUi(self, FileReplicants):
        _translate = QtCore.QCoreApplication.translate
        FileReplicants.setWindowTitle(_translate("FileReplicants", "File Replicants"))
        self.BtnLoadDir.setText(_translate("FileReplicants", "LoadDir"))
        self.WorkAreaAnalysisGrp.setTitle(_translate("FileReplicants", "Work Area Analysis"))
        self.FileList.setSortingEnabled(True)
        self.FileList.headerItem().setText(0, _translate("FileReplicants", "Files"))
        self.FileList.headerItem().setText(1, _translate("FileReplicants", "Hash"))
        self.FileList.headerItem().setText(2, _translate("FileReplicants", "Size"))
        self.FileList.headerItem().setText(3, _translate("FileReplicants", "Count"))
        __sortingEnabled = self.FileList.isSortingEnabled()
        self.FileList.setSortingEnabled(False)
        self.FileList.topLevelItem(0).setText(0, _translate("FileReplicants", "FileName2"))
        self.FileList.topLevelItem(0).setText(1, _translate("FileReplicants", "smnmkhslkd"))
        self.FileList.topLevelItem(0).setText(2, _translate("FileReplicants", "2038"))
        self.FileList.topLevelItem(0).setText(3, _translate("FileReplicants", "1"))
        self.FileList.topLevelItem(0).child(0).setText(0, _translate("FileReplicants", "location"))
        self.FileList.topLevelItem(1).setText(0, _translate("FileReplicants", "Filename"))
        self.FileList.topLevelItem(1).setText(1, _translate("FileReplicants", "skjhffkdsjfhskdjf"))
        self.FileList.topLevelItem(1).setText(2, _translate("FileReplicants", "1025"))
        self.FileList.topLevelItem(1).setText(3, _translate("FileReplicants", "2"))
        self.FileList.topLevelItem(1).child(0).setText(0, _translate("FileReplicants", "location2"))
        self.FileList.topLevelItem(1).child(1).setText(0, _translate("FileReplicants", "location1"))
        self.FileList.setSortingEnabled(__sortingEnabled)
        self.BtnClearDebug.setText(_translate("FileReplicants", "Clear Debug"))
        self.BtnClearList.setText(_translate("FileReplicants", "Clear List"))
        self.BtnAnalysis.setText(_translate("FileReplicants", "Analyse"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileReplicants = QtWidgets.QMainWindow()
    ui = Ui_FileReplicants()
    ui.setupUi(FileReplicants)
    FileReplicants.show()
    sys.exit(app.exec_())
