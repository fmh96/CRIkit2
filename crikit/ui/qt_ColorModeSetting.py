# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_ColorModeSettings.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(159, 213)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 20))
        Form.setMaximumSize(QtCore.QSize(16777215, 263))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 20))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutImgColors = QtWidgets.QVBoxLayout()
        self.verticalLayoutImgColors.setContentsMargins(2, 2, 2, 2)
        self.verticalLayoutImgColors.setSpacing(2)
        self.verticalLayoutImgColors.setObjectName("verticalLayoutImgColors")
        self.labelColorMode = QtWidgets.QLabel(self.frame)
        self.labelColorMode.setObjectName("labelColorMode")
        self.verticalLayoutImgColors.addWidget(self.labelColorMode)
        self.comboBoxColorMode = QtWidgets.QComboBox(self.frame)
        self.comboBoxColorMode.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxColorMode.setObjectName("comboBoxColorMode")
        self.comboBoxColorMode.addItem("")
        self.comboBoxColorMode.addItem("")
        self.verticalLayoutImgColors.addWidget(self.comboBoxColorMode)
        self.labelFGColor = QtWidgets.QLabel(self.frame)
        self.labelFGColor.setObjectName("labelFGColor")
        self.verticalLayoutImgColors.addWidget(self.labelFGColor)
        self.comboBoxFGColor = QtWidgets.QComboBox(self.frame)
        self.comboBoxFGColor.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxFGColor.setObjectName("comboBoxFGColor")
        self.verticalLayoutImgColors.addWidget(self.comboBoxFGColor)
        self.labelBGColor = QtWidgets.QLabel(self.frame)
        self.labelBGColor.setObjectName("labelBGColor")
        self.verticalLayoutImgColors.addWidget(self.labelBGColor)
        self.comboBoxBGColor = QtWidgets.QComboBox(self.frame)
        self.comboBoxBGColor.setMinimumSize(QtCore.QSize(120, 30))
        self.comboBoxBGColor.setObjectName("comboBoxBGColor")
        self.verticalLayoutImgColors.addWidget(self.comboBoxBGColor)
        self.labelColormap = QtWidgets.QLabel(self.frame)
        self.labelColormap.setObjectName("labelColormap")
        self.verticalLayoutImgColors.addWidget(self.labelColormap)
        self.comboBoxColormap = QtWidgets.QComboBox(self.frame)
        self.comboBoxColormap.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxColormap.setObjectName("comboBoxColormap")
        self.verticalLayoutImgColors.addWidget(self.comboBoxColormap)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutImgColors.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayoutImgColors)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelColorMode.setText(_translate("Form", "Color Mode"))
        self.comboBoxColorMode.setItemText(0, _translate("Form", "RGB"))
        self.comboBoxColorMode.setItemText(1, _translate("Form", "Colormap"))
        self.labelFGColor.setText(_translate("Form", "Image Color"))
        self.labelBGColor.setText(_translate("Form", "Background Color"))
        self.labelColormap.setText(_translate("Form", "Colormap"))
