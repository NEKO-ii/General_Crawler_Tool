# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SettingPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout, QWidget)


class Ui_SettingPage(object):

    def setupUi(self, SettingPage):
        if not SettingPage.objectName():
            SettingPage.setObjectName(u"SettingPage")
        self.verticalLayout_2 = QVBoxLayout(SettingPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hly_top = QHBoxLayout()
        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_top.addItem(self.hs_1)

        self.btn_default = QPushButton(SettingPage)
        self.hly_top.addWidget(self.btn_default)

        self.btn_apply = QPushButton(SettingPage)
        self.hly_top.addWidget(self.btn_apply)

        self.verticalLayout_2.addLayout(self.hly_top)

        self.hly_L1 = QHBoxLayout()
        self.gly_1 = QGridLayout()
        self.gly_1.setVerticalSpacing(6)
        self.check_sleep = QCheckBox(SettingPage)
        self.gly_1.addWidget(self.check_sleep, 0, 0, 1, 1)

        self.lb_1 = QLabel(SettingPage)
        self.gly_1.addWidget(self.lb_1, 0, 1, 1, 1)

        self.spin_sleepTime = QSpinBox(SettingPage)
        self.gly_1.addWidget(self.spin_sleepTime, 0, 2, 1, 1)

        self.check_parseMsgOut = QCheckBox(SettingPage)
        self.gly_1.addWidget(self.check_parseMsgOut, 1, 0, 1, 1)

        self.lb_2 = QLabel(SettingPage)
        self.gly_1.addWidget(self.lb_2, 1, 1, 1, 1)

        self.combo_parseOutMsgType = QComboBox(SettingPage)
        self.combo_parseOutMsgType.addItem("")
        self.combo_parseOutMsgType.addItem("")
        self.combo_parseOutMsgType.addItem("")
        self.gly_1.addWidget(self.combo_parseOutMsgType, 1, 2, 1, 1)

        self.check_asyn = QCheckBox(SettingPage)
        self.gly_1.addWidget(self.check_asyn, 2, 0, 1, 1)

        self.lb_3 = QLabel(SettingPage)
        self.gly_1.addWidget(self.lb_3, 2, 1, 1, 1)

        self.spin_asynCount = QSpinBox(SettingPage)
        self.gly_1.addWidget(self.spin_asynCount, 2, 2, 1, 1)

        self.hly_L1.addLayout(self.gly_1)

        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_L1.addItem(self.hs_2)

        self.verticalLayout_2.addLayout(self.hly_L1)

        self.gly_L2 = QGridLayout()
        self.lb_4 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_4, 0, 0, 1, 1)

        self.ledit_importPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_importPath, 0, 1, 1, 1)

        self.btn_importPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_importPathSet, 0, 2, 1, 1)

        self.lb_5 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_5, 1, 0, 1, 1)

        self.ledit_exportPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_exportPath, 1, 1, 1, 1)

        self.btn_exportPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_exportPathSet, 1, 2, 1, 1)

        self.lb_6 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_6, 2, 0, 1, 1)

        self.ledit_configPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_configPath, 2, 1, 1, 1)

        self.btn_configPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_configPathSet, 2, 2, 1, 1)

        self.lb_7 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_7, 3, 0, 1, 1)

        self.ledit_scriptPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_scriptPath, 3, 1, 1, 1)

        self.btn_scriptPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_scriptPathSet, 3, 2, 1, 1)

        self.lb_8 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_8, 4, 0, 1, 1)

        self.ledit_tempPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_tempPath, 4, 1, 1, 1)

        self.btn_tempPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_tempPathSet, 4, 2, 1, 1)

        self.lb_9 = QLabel(SettingPage)
        self.gly_L2.addWidget(self.lb_9, 5, 0, 1, 1)

        self.ledit_logPath = QLineEdit(SettingPage)
        self.gly_L2.addWidget(self.ledit_logPath, 5, 1, 1, 1)

        self.btn_logPathSet = QPushButton(SettingPage)
        self.gly_L2.addWidget(self.btn_logPathSet, 5, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gly_L2)

        self.hly_L3 = QHBoxLayout()
        self.verticalLayout = QVBoxLayout()
        self.check_logEnable = QCheckBox(SettingPage)
        self.verticalLayout.addWidget(self.check_logEnable)

        self.check_hideTitleBar = QCheckBox(SettingPage)
        self.verticalLayout.addWidget(self.check_hideTitleBar)

        self.hly_L3.addLayout(self.verticalLayout)

        self.hs_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_L3.addItem(self.hs_3)

        self.verticalLayout_2.addLayout(self.hly_L3)

        self.hly_L4 = QHBoxLayout()
        self.gly_2 = QGridLayout()
        self.lb_10 = QLabel(SettingPage)
        self.gly_2.addWidget(self.lb_10, 0, 0, 1, 1)

        self.lb_11 = QLabel(SettingPage)
        self.gly_2.addWidget(self.lb_11, 1, 0, 1, 1)

        self.lb_12 = QLabel(SettingPage)
        self.gly_2.addWidget(self.lb_12, 2, 0, 1, 1)

        self.lb_13 = QLabel(SettingPage)
        self.gly_2.addWidget(self.lb_13, 3, 0, 1, 1)

        self.spin_fontsize_menu = QSpinBox(SettingPage)
        self.gly_2.addWidget(self.spin_fontsize_menu, 1, 1, 1, 1)

        self.spin_fontsize_editor = QSpinBox(SettingPage)
        self.gly_2.addWidget(self.spin_fontsize_editor, 2, 1, 1, 1)

        self.combo_theme = QComboBox(SettingPage)
        self.combo_theme.addItem("")
        self.gly_2.addWidget(self.combo_theme, 3, 1, 1, 1)

        self.combo_font = QFontComboBox(SettingPage)
        self.gly_2.addWidget(self.combo_font, 0, 1, 1, 1)

        self.hly_L4.addLayout(self.gly_2)

        self.hs_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hly_L4.addItem(self.hs_4)

        self.verticalLayout_2.addLayout(self.hly_L4)

        self.vs_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.vs_bottom)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(SettingPage)

    # setupUi

    def retranslateUi(self):
        self.btn_default.setText(QCoreApplication.translate("SettingPage", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.btn_apply.setText(QCoreApplication.translate("SettingPage", u"\u5e94\u7528", None))
        self.check_sleep.setText(QCoreApplication.translate("SettingPage", u"\u542f\u7528\u8bf7\u6c42\u95f4\u9694", None))
        self.lb_1.setText(QCoreApplication.translate("SettingPage", u"\u95f4\u9694\u65f6\u95f4", None))
        self.check_parseMsgOut.setText(QCoreApplication.translate("SettingPage", u"\u542f\u7528\u6570\u636e\u5904\u7406\u6d88\u606f\u8f93\u51fa", None))
        self.lb_2.setText(QCoreApplication.translate("SettingPage", u"\u6d88\u606f\u6a21\u5f0f", None))
        self.combo_parseOutMsgType.setItemText(0, QCoreApplication.translate("SettingPage", u"\u4ec5\u8f93\u51fa\u9519\u8bef\u6d88\u606f", None))
        self.combo_parseOutMsgType.setItemText(1, QCoreApplication.translate("SettingPage", u"\u8f93\u51fa\u9519\u8bef\u4e0e\u8b66\u544a", None))
        self.combo_parseOutMsgType.setItemText(2, QCoreApplication.translate("SettingPage", u"\u8f93\u51fa\u5168\u90e8\u6d88\u606f", None))

        self.check_asyn.setText(QCoreApplication.translate("SettingPage", u"\u542f\u7528\u5f02\u6b65\u8bf7\u6c42", None))
        self.lb_3.setText(QCoreApplication.translate("SettingPage", u"\u6700\u5927\u534f\u7a0b\u6570\u91cf", None))
        self.lb_4.setText(QCoreApplication.translate("SettingPage", u"\u6587\u4ef6\u5bfc\u5165\u8def\u5f84", None))
        self.btn_importPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_5.setText(QCoreApplication.translate("SettingPage", u"\u6587\u4ef6\u5bfc\u51fa\u8def\u5f84", None))
        self.btn_exportPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_6.setText(QCoreApplication.translate("SettingPage", u"\u914d\u7f6e\u6587\u4ef6\u8def\u5f84", None))
        self.btn_configPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_7.setText(QCoreApplication.translate("SettingPage", u"\u811a\u672c\u6587\u4ef6\u8def\u5f84", None))
        self.btn_scriptPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_8.setText(QCoreApplication.translate("SettingPage", u"\u4e34\u65f6\u6587\u4ef6\u8def\u5f84", None))
        self.btn_tempPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.lb_9.setText(QCoreApplication.translate("SettingPage", u"\u65e5\u5fd7\u6587\u4ef6\u8def\u5f84", None))
        self.btn_logPathSet.setText(QCoreApplication.translate("SettingPage", u"\u9009\u62e9\u8def\u5f84", None))
        self.check_logEnable.setText(QCoreApplication.translate("SettingPage", u"\u542f\u7528\u65e5\u5fd7\u8bb0\u5f55", None))
        self.check_hideTitleBar.setText(QCoreApplication.translate("SettingPage", u"\u9690\u85cf\u7cfb\u7edf\u5bfc\u822a\u680f", None))
        self.lb_10.setText(QCoreApplication.translate("SettingPage", u"\u5b57\u4f53", None))
        self.lb_11.setText(QCoreApplication.translate("SettingPage", u"\u83dc\u5355\u5b57\u53f7", None))
        self.lb_12.setText(QCoreApplication.translate("SettingPage", u"\u8f93\u5165\u6846\u5b57\u53f7", None))
        self.lb_13.setText(QCoreApplication.translate("SettingPage", u"\u7cfb\u7edf\u4e3b\u9898", None))
        self.combo_theme.setItemText(0, QCoreApplication.translate("SettingPage", u"\u6697\u8272", None))

    # retranslateUi
