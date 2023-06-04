# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalysisPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from ui.widgets import GroupBox, PushButton, SpinBox, LineEdit, TableWidget


class Ui_AnalysisPage(object):

    def setupUi(self, AnalysisPage):
        if not AnalysisPage.objectName():
            AnalysisPage.setObjectName(u"AnalysisPage")
        self.vly1 = QVBoxLayout(AnalysisPage)
        self.vly1.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.btn_selectFile = PushButton(AnalysisPage, type="primary")
        self.hly_top.addWidget(self.btn_selectFile)

        self.btn_selectTD = PushButton(AnalysisPage, type="primary")
        self.hly_top.addWidget(self.btn_selectTD)

        self.btn_clearData = PushButton(AnalysisPage, type="error")
        self.hly_top.addWidget(self.btn_clearData)

        self.ledit_filePath = LineEdit(AnalysisPage)
        self.ledit_filePath.setMinimumWidth(600)
        self.ledit_filePath.setReadOnly(True)
        self.ledit_filePath.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.hly_top.addWidget(self.ledit_filePath)

        self.hs1 = QSpacerItem(508, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(self.hs1)

        self.btn_run = PushButton(AnalysisPage, type="success")
        self.hly_top.addWidget(self.btn_run)

        self.vly1.addLayout(self.hly_top)

        self.group_settings = GroupBox(AnalysisPage)
        sizePolicy_1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(1)
        sizePolicy_1.setHeightForWidth(self.group_settings.sizePolicy().hasHeightForWidth())
        self.group_settings.setSizePolicy(sizePolicy_1)

        self.hly2 = QHBoxLayout(self.group_settings)
        self.hly2.setContentsMargins(-1, 9, -1, -1)
        self.vly2 = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.label = QLabel(self.group_settings)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spin_xindex = SpinBox(self.group_settings)
        self.spin_xindex.setMinimumWidth(40)
        self.spin_xindex.setMinimum(1)
        self.gridLayout.addWidget(self.spin_xindex, 0, 1, 1, 1)

        self.check_x = QCheckBox(self.group_settings)
        self.gridLayout.addWidget(self.check_x, 0, 2, 1, 1)

        self.label_2 = QLabel(self.group_settings)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spin_yindex = SpinBox(self.group_settings)
        self.spin_yindex.setMinimumWidth(40)
        self.spin_yindex.setMinimum(1)
        self.gridLayout.addWidget(self.spin_yindex, 1, 1, 1, 1)

        self.check_y = QCheckBox(self.group_settings)
        self.gridLayout.addWidget(self.check_y, 1, 2, 1, 1)

        self.vly2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vly2.addItem(self.verticalSpacer)

        self.hly2.addLayout(self.vly2)

        self.table_data = TableWidget(self.group_settings, extendHeight=True)
        self.table_data.setEditTriggers(TableWidget.EditTrigger.NoEditTriggers)
        self.hly2.addWidget(self.table_data)

        self.vly1.addWidget(self.group_settings)

        self.group_pic = GroupBox(AnalysisPage)
        sizePolicy_2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(1)
        sizePolicy_2.setHeightForWidth(self.group_pic.sizePolicy().hasHeightForWidth())
        self.group_pic.setSizePolicy(sizePolicy_2)

        self.vly_pic = QVBoxLayout(self.group_pic)

        self.vly1.addWidget(self.group_pic)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(AnalysisPage)

    # setupUi

    def retranslateUi(self):
        self.btn_selectFile.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.btn_selectTD.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u4e34\u65f6\u6570\u636e", None))
        self.btn_clearData.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u6570\u636e", None))
        self.btn_run.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5206\u6790", None))
        self.group_settings.setTitle(QCoreApplication.translate("Form", u"\u76f8\u5173\u6027\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("Form", u"X\u8f74\u6570\u636e\u5217\u7d22\u5f15", None))
        self.check_x.setText(QCoreApplication.translate("Form", u"\u542b\u6709\u6587\u5b57", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Y\u8f74\u6570\u636e\u5217\u7d22\u5f15", None))
        self.check_y.setText(QCoreApplication.translate("Form", u"\u542b\u6709\u6587\u5b57", None))
        self.group_pic.setTitle(QCoreApplication.translate("Form", u"\u56fe\u8868", None))

    # retranslateUi
