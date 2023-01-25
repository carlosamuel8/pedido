from PySide6 import QtWidgets
from ui_main import Ui_MainWindow
from PySide6.QtCore import QEvent

import random

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)

        self.btnao.clicked.connect(self.moveButton)

        self.frameNAO.installEventFilter(self)

        self.btsim.clicked.connect(self.visibleCoracao)




    def visibleCoracao(self):
        self.pergunta.setText("Escolheu a melhor opção 😍")
        self.btsim.setVisible(False)
        self.btnao.setVisible(False)
        self.coracao.setVisible(True)

    def moveButton(self):
        self.frameNAO.move(random.randint(0, 300), random.randint(0, 300))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frameNAO:
            self.moveButton()
            return True
        else:
            return False
    
        



app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec_()

    