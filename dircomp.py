from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from DirShaComp import Ui_FileReplicants
import os
from lxml import etree


class qtapp(Ui_FileReplicants):
    '''
    qtapp : Inherits from Ui_FileReplicants Class

    '''
    Tree = etree.Element('root')

    currentDir = os.getcwd()

    def __init__(self, FileReplicants):
        self.setupUi(FileReplicants)
        self.InputWorkDir.setEnabled(False)
        self.FileReplicants = FileReplicants
        FileReplicants.show()
        self.changeWorkingDir(self.currentDir)
        self.BtnLoadDir.clicked.connect(self.changeWorkingDir)
        self.BtnAnalysis.clicked.connect(self.analyseWorkingDir)
        self.BtnClearDebug.clicked.connect(self.ProcessDebug.clear)

    def analyseWorkingDir(self):
        for root, dirs, files in os.walk(self.currentDir):
            rowMsg = "{0} consumes [{1}] [{2}]\n".format(root, dirs, files)
            self.ProcessDebug.appendPlainText(rowMsg)

    def changeWorkingDir(self, directory=None):
        # self.currentDir=
        print(type(directory))
        if type(directory) != bool:

            if directory is not None and len(directory) != 0:
                self.currentDir = directory
            else:
                SelectedDIR = QFileDialog.getExistingDirectory(
                    None, 'Select Directory ', self.currentDir,
                    QtWidgets.QFileDialog.ShowDirsOnly)
                if len(SelectedDIR) != 0:
                    self.currentDir = SelectedDIR
        else:
            SelectedDIR = QFileDialog.getExistingDirectory(
                None, 'Select Directory ', self.currentDir,
                QtWidgets.QFileDialog.ShowDirsOnly)
            if len(SelectedDIR) != 0:
                self.currentDir = SelectedDIR
        self.InputWorkDir.setText(self.currentDir)
        self.ProcessDebug.appendPlainText(
            "#########################\n{0}\n#########################".format(
                self.currentDir))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileReplicants = QtWidgets.QMainWindow()
    ui = qtapp(FileReplicants)
    sys.exit(app.exec_())
