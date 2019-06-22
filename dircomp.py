from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from DirShaComp import Ui_FileReplicants
import os
from lxml import etree
from hashlib import md5


BufferSize = 1024


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

    def readfileHash(self, file2read):
        myhash = md5()
        with open(file2read, "rb") as fd:
            bytesRead = fd.read(BufferSize)
            while len(bytesRead) > 0:
                myhash.update(bytesRead)
                bytesRead = fd.read(BufferSize)
            return myhash.hexdigest()

    def analyseWorkingDir(self):
        for root, dirs, files in os.walk(self.currentDir):
            rowMsg = "{0}<-root \n\t[{1}] <-dirs\n\t\t[{2}] \n".format(
                root,
                dirs,
                files
            )
            self.ProcessDebug.appendPlainText(rowMsg)
            # print(rowMsg)
            """
                Next we shall be appending the file to the XML
            """
            for thefile in files:
                file2read = os.path.join(root, thefile)
                hashedFile = self.readfileHash(file2read)
                self.ProcessDebug.appendPlainText(
                    "Hashed = {0}".format(
                        hashedFile
                    )
                )
                """
                Next Search for hashed File if found in document
                if found in document then append the data to it
                else create a new node and append it
                """
                hashedElement = self.Tree.find("h_{0}".format(hashedFile))
                if etree.iselement(hashedElement):
                    # print(
                    #     "Duplicate => {0} {1}".format(
                    #         hashedElement.find('File').text,
                    #         file2read
                    #     )
                    # )
                    pass
                else:
                    hashedElement = etree.Element("h_{0}".format(hashedFile))
                El = etree.Element('File')
                El.text = file2read
                hashedElement.append(El)
                self.Tree.append(hashedElement)
        # print(etree.tostring(self.Tree, encoding=str))
        self.ProcessDebug.appendPlainText(
            etree.tostring(
                self.Tree,
                encoding=str
            )
        )

    def changeWorkingDir(self, directory=None):
        # self.currentDir=
        print(type(directory))
        if not isinstance(directory, bool):

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
