# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.113636 rgba(228, 0, 0, 255), stop:0.539773 rgba(176, 33, 8, 255), stop:0.982955 rgba(189, 4, 4, 255));\n"
"}\n"
"\n"
"QLabel#pergunta{\n"
"	font-size:35px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 2px solid white;\n"
"	background-color: white;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	color: red;\n"
"	min-height: 45px;\n"
"	border-radius: 15px\n"
"}")
        self.pergunta = QLabel(self.centralwidget)
        self.pergunta.setObjectName(u"pergunta")
        self.pergunta.setGeometry(QRect(0, 50, 601, 81))
        self.pergunta.setAlignment(Qt.AlignCenter)
        self.frameSIM = QFrame(self.centralwidget)
        self.frameSIM.setObjectName(u"frameSIM")
        self.frameSIM.setGeometry(QRect(130, 200, 131, 71))
        self.frameSIM.setFrameShape(QFrame.NoFrame)
        self.frameSIM.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSIM)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btsim = QPushButton(self.frameSIM)
        self.btsim.setObjectName(u"btsim")
        self.btsim.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btsim)

        self.frameNAO = QFrame(self.centralwidget)
        self.frameNAO.setObjectName(u"frameNAO")
        self.frameNAO.setGeometry(QRect(310, 200, 131, 71))
        self.frameNAO.setMinimumSize(QSize(131, 71))
        self.frameNAO.setFrameShape(QFrame.NoFrame)
        self.frameNAO.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameNAO)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnao = QPushButton(self.frameNAO)
        self.btnao.setObjectName(u"btnao")
        self.btnao.setMinimumSize(QSize(113, 49))

        self.horizontalLayout_2.addWidget(self.btnao)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(120, 80, 341, 331))
        self.coracao.setPixmap(QPixmap(u":/imagens/coracao.png"))
        self.coracao.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pergunta.setText(QCoreApplication.translate("MainWindow", u"Quer namorar comigo?", None))
        self.btsim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btnao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.coracao.setText("")
    # retranslateUi

