# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(886, 617)
        Dialog.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img = QLabel(Dialog)
        self.img.setObjectName(u"img")
        self.img.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout.addWidget(self.img)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.reset = QPushButton(Dialog)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout_2.addWidget(self.reset)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.adress = QLabel(Dialog)
        self.adress.setObjectName(u"adress")

        self.horizontalLayout_2.addWidget(self.adress)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search = QPushButton(Dialog)
        self.search.setObjectName(u"search")

        self.horizontalLayout.addWidget(self.search)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.img.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441\u043b\u043e\u0439", None))
        self.reset.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u043e\u0433\u043e \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441", None))
        self.adress.setText("")
        self.search.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

