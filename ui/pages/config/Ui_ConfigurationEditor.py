# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_config_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtWidgets import (QAbstractSpinBox, QTableWidget, QCheckBox, QComboBox, QFormLayout, QFrame, QGroupBox, QHBoxLayout, QLabel, QListWidget, QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

from core.sys import Themes, Globalv, GlvKey
from ui.widgets import (ComboBox, LineEdit, List, PushButton, ScrollArea, SpinBox, TableWidget, TextEdit, GroupBox)


class Ui_ConfigurationEditor(object):

    def __init__(self, ConfigurationEditor: QWidget) -> None:
        self.themes: Themes = Globalv.get(GlvKey.THEMES)
        self.style = F'''
        #edit_place_WidgetContents {{
            background-color: {self.themes.color["bg_1"]};
            border: 1px solid {self.themes.color["dark_3"]};
        }}
        #line {{
            background-color: {self.themes.color["bg_3"]};
        }}
        QLabel:enabled {{
            color: {self.themes.color["text_foreground"]};
        }}
        QLabel:disabled {{
            color: {self.themes.color["text_description"]};
        }}
        '''
        self.setupUi(ConfigurationEditor)
        ConfigurationEditor.setStyleSheet(self.style)
        self._setScrollParent(ConfigurationEditor)
        self._setTableHeader()

    def _setScrollParent(self, ConfigurationEditor: QWidget) -> None:
        for item in ConfigurationEditor.findChildren(QComboBox):
            item.c_setScrollParent(self.editPlace)
        for item in ConfigurationEditor.findChildren(QTextEdit):
            item.c_setScrollParent(self.editPlace)
        for item in ConfigurationEditor.findChildren(QSpinBox):
            item.c_setScrollParent(self.editPlace)
        for item in ConfigurationEditor.findChildren(QListWidget):
            item.c_setScrollParent(self.editPlace)
        for item in ConfigurationEditor.findChildren(QTableWidget):
            item.c_setScrollParent(self.editPlace)

    def _setTableHeader(self) -> None:
        self.table_parameter.c_setHeader(["参数名", "参数值"])
        self.table_headers.c_setHeader(["参数名", "参数值"])
        self.table_headers.setColumnWidth(0, 200)
        self.table_dataForm.c_setHeader(["参数名", "参数值"])
        self.table_dataForm_script.c_setHeader(["参数名", "来源模块", "输入参数", "输出列表索引"])
        self.table_dataForm_script.c_setHeaderTooltip([None, "该参数名对应的值由哪个模块输出\n输入模块名(需要后缀)", "若该模块需要输入参数则在此填写\n若不需要则留空", "若该模块输出一个列表而参数值只需要其中一项\n在此处输入该项的索引(起始为1)"])
        self.table_cookies.c_setHeader(["键", "值"])
        self.table_cookies.setColumnWidth(0, 200)
        self.table_psetText.c_setHeader(["方法", "匹配语法", "索引值", "间隔字符"])
        self.table_psetText.c_setColWidth([120, 700, 200])
        self.table_psetText.c_setHeaderTooltip(["文本匹配方式\nRE:正则表达式匹配\nBS4:BeautifulSoup标签搜索语法\nXPATH:XML路径定位语法", "所选方法对应的匹配语句", "若前面的语法匹配到的结果不止一个\n可在此填写所需结果的索引\n(起始为0,空表示选择所有,可多选索引间用逗号分隔)", "若有多个匹配结果,可在此填写多个结果间的分隔符\n默认为空代表空格"])

    def setupUi(self, ConfigurationEditor: QWidget):
        if not ConfigurationEditor.objectName():
            ConfigurationEditor.setObjectName(u"ConfigurationEditor")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigurationEditor.sizePolicy().hasHeightForWidth())
        ConfigurationEditor.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ConfigurationEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(ConfigurationEditor)
        self.topBar.setObjectName(u"top_bar")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_back = PushButton(self.topBar)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_2.addWidget(self.btn_back)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btn_default = PushButton(self.topBar, text="恢复默认", type="warning")
        self.btn_default.setObjectName(u"btn_default")
        self.horizontalLayout_2.addWidget(self.btn_default)

        self.btn_editInJson = PushButton(self.topBar, type="primary")
        self.btn_editInJson.setObjectName(u"btn_edit_json")
        self.horizontalLayout_2.addWidget(self.btn_editInJson)

        self.btn_save = PushButton(self.topBar, type="success")
        self.btn_save.setObjectName(u"btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)

        self.verticalLayout.addWidget(self.topBar)

        self.editPlace = ScrollArea(ConfigurationEditor)
        self.editPlace.setObjectName(u"edit_place")
        self.editPlace.setWidgetResizable(True)
        self.editPlace_WidgetContents = QWidget()
        self.editPlace_WidgetContents.setObjectName(u"edit_place_WidgetContents")
        self.editPlace_WidgetContents.setGeometry(QRect(0, 0, 887, 1375))
        self.verticalLayout_2 = QVBoxLayout(self.editPlace_WidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.group_url = GroupBox(self.editPlace_WidgetContents)
        self.group_url.setObjectName(u"group_url")
        sizePolicy.setHeightForWidth(self.group_url.sizePolicy().hasHeightForWidth())
        self.group_url.setSizePolicy(sizePolicy)
        self.group_url.setMinimumSize(QSize(0, 250))
        self.group_url.setMaximumSize(QSize(16777215, 16777215))
        self.group_url.setFlat(False)
        self.group_url.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.group_url)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.urlSet = QFrame(self.group_url)
        self.urlSet.setObjectName(u"url_set")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.urlSet.sizePolicy().hasHeightForWidth())
        self.urlSet.setSizePolicy(sizePolicy1)
        self.urlSet.setMinimumSize(QSize(0, 0))
        self.urlSet.setMaximumSize(QSize(16777215, 16777215))
        self.urlSet.setFrameShape(QFrame.StyledPanel)
        self.urlSet.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.urlSet)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.urlSet_topLayout = QHBoxLayout()
        self.urlSet_topLayout.setObjectName(u"url_set_top_layout")
        self.urlSet_lable1 = QLabel(self.urlSet)
        self.urlSet_lable1.setObjectName(u"url_set_lable1")

        self.urlSet_topLayout.addWidget(self.urlSet_lable1)

        self.combo_urlSource = ComboBox(self.urlSet)
        self.combo_urlSource.addItem("")
        self.combo_urlSource.addItem("")
        self.combo_urlSource.setObjectName(u"combo_url_source")

        self.urlSet_topLayout.addWidget(self.combo_urlSource)

        self.ledit_urlSource = LineEdit(self.urlSet, placeHolderText="输入网址基本路径")
        self.ledit_urlSource.setObjectName(u"ledit_url_source")

        self.urlSet_topLayout.addWidget(self.ledit_urlSource)

        self.btn_chooseFile = PushButton(self.urlSet, "文件")
        self.btn_chooseFile.setEnabled(False)
        self.btn_chooseFile.setObjectName(u"btn_choose_file")
        self.urlSet_topLayout.addWidget(self.btn_chooseFile)

        self.btn_urlSetConfirm = PushButton(self.urlSet, type="primary")
        self.btn_urlSetConfirm.setObjectName(u"btn_url_set_confirm")

        self.urlSet_topLayout.addWidget(self.btn_urlSetConfirm)

        self.verticalLayout_8.addLayout(self.urlSet_topLayout)

        self.urlSet_bottomLayout = QHBoxLayout()
        self.urlSet_bottomLayout.setObjectName(u"url_set_bottom_layout")
        self.group_parameter = GroupBox(self.urlSet)
        self.group_parameter.setObjectName(u"group_parameter")
        sizePolicy1.setHeightForWidth(self.group_parameter.sizePolicy().hasHeightForWidth())
        self.group_parameter.setSizePolicy(sizePolicy1)
        self.group_parameter.setMinimumSize(QSize(0, 0))
        self.group_parameter.setMaximumSize(QSize(16777215, 16777215))
        self.group_parameter.setCheckable(True)
        self.group_parameter.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.group_parameter)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.parameterBtnLayout = QHBoxLayout()
        self.parameterBtnLayout.setObjectName(u"parameter_btn_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.parameterBtnLayout.addItem(self.horizontalSpacer_2)

        self.btn_parameterAdd = PushButton(self.group_parameter)
        self.btn_parameterAdd.setObjectName(u"btn_parameter_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_parameterAdd.sizePolicy().hasHeightForWidth())
        self.btn_parameterAdd.setSizePolicy(sizePolicy2)
        self.btn_parameterAdd.setMaximumSize(QSize(16777215, 16777215))

        self.parameterBtnLayout.addWidget(self.btn_parameterAdd)

        self.btn_parameterDelete = PushButton(self.group_parameter)
        self.btn_parameterDelete.setObjectName(u"btn_parameter_delete")
        self.btn_parameterDelete.setMaximumSize(QSize(16777215, 16777215))

        self.parameterBtnLayout.addWidget(self.btn_parameterDelete)

        self.verticalLayout_5.addLayout(self.parameterBtnLayout)

        self.table_parameter = TableWidget(self.group_parameter)
        self.table_parameter.setObjectName(u"table_parameter")
        self.table_parameter.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.table_parameter)

        self.urlSet_bottomLayout.addWidget(self.group_parameter)

        self.group_iteration = GroupBox(self.urlSet)
        self.group_iteration.setObjectName(u"group_iteration")
        sizePolicy1.setHeightForWidth(self.group_iteration.sizePolicy().hasHeightForWidth())
        self.group_iteration.setSizePolicy(sizePolicy1)
        self.group_iteration.setCheckable(True)
        self.group_iteration.setChecked(False)
        self.formLayout = QFormLayout(self.group_iteration)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.iteration_lable1 = QLabel(self.group_iteration)
        self.iteration_lable1.setObjectName(u"iteration_lable1")
        self.iteration_lable1.setLayoutDirection(Qt.LeftToRight)
        self.iteration_lable1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.iteration_lable1)

        self.ledit_iterationName = LineEdit(self.group_iteration)
        self.ledit_iterationName.setObjectName(u"ledit_iteration_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_iterationName)

        self.iteration_lable2 = QLabel(self.group_iteration)
        self.iteration_lable2.setObjectName(u"iteration_lable2")
        self.iteration_lable2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.iteration_lable2)

        self.ledit_iterationStart = LineEdit(self.group_iteration)
        self.ledit_iterationStart.setObjectName(u"ledit_iteration_start")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_iterationStart)

        self.iteration_lable3 = QLabel(self.group_iteration)
        self.iteration_lable3.setObjectName(u"iteration_lable3")
        self.iteration_lable3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.iteration_lable3)

        self.ledit_iterationStop = LineEdit(self.group_iteration)
        self.ledit_iterationStop.setObjectName(u"ledit_iteration_stop")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ledit_iterationStop)

        self.iteration_lable4 = QLabel(self.group_iteration)
        self.iteration_lable4.setObjectName(u"iteration_lable4")
        self.iteration_lable4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.iteration_lable4)

        self.ledit_iterationStep = LineEdit(self.group_iteration)
        self.ledit_iterationStep.setObjectName(u"ledit_iteration_step")
        self.ledit_iterationStep.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ledit_iterationStep)

        self.urlSet_bottomLayout.addWidget(self.group_iteration)

        self.verticalLayout_8.addLayout(self.urlSet_bottomLayout)

        self.horizontalLayout.addWidget(self.urlSet)

        self.line = QFrame(self.group_url)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.urlView = QFrame(self.group_url)
        self.urlView.setObjectName(u"url_view")
        self.urlView.setFrameShape(QFrame.StyledPanel)
        self.urlView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.urlView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.urlView_topLayout = QHBoxLayout()
        self.urlView_topLayout.setObjectName(u"url_view_top_layout")
        self.urlView_lable1 = QLabel(self.urlView)
        self.urlView_lable1.setObjectName(u"url_view_lable1")

        self.urlView_topLayout.addWidget(self.urlView_lable1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.urlView_topLayout.addItem(self.horizontalSpacer)

        self.urlView_lable2 = QLabel(self.urlView)
        self.urlView_lable2.setObjectName(u"url_view_lable2")
        self.urlView_lable2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.urlView_topLayout.addWidget(self.urlView_lable2)

        self.ledit_urlView_count = LineEdit(self.urlView, color_enabled="rgb(17, 169, 225)")
        self.ledit_urlView_count.setObjectName(u"ledit_url_view_count")
        self.ledit_urlView_count.setEnabled(True)
        self.ledit_urlView_count.setMinimumSize(QSize(60, 0))
        self.ledit_urlView_count.setMaximumSize(QSize(60, 16777215))
        self.ledit_urlView_count.setReadOnly(True)
        self.ledit_urlView_count.setFocusPolicy(Qt.NoFocus)

        self.urlView_topLayout.addWidget(self.ledit_urlView_count)

        self.btn_urlView_add = PushButton(self.urlView)
        self.btn_urlView_add.setObjectName(u"btn_url_view_add")
        self.btn_urlView_add.setMaximumSize(QSize(70, 16777215))

        self.urlView_topLayout.addWidget(self.btn_urlView_add)

        self.btn_urlView_delete = PushButton(self.urlView)
        self.btn_urlView_delete.setObjectName(u"btn_url_view_delete")
        self.btn_urlView_delete.setMaximumSize(QSize(70, 16777215))

        self.urlView_topLayout.addWidget(self.btn_urlView_delete)

        self.verticalLayout_3.addLayout(self.urlView_topLayout)

        self.list_urlView = List(self.urlView)
        self.list_urlView.setObjectName(u"list_url_view")
        self.list_urlView.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.list_urlView)

        self.horizontalLayout.addWidget(self.urlView)

        self.verticalLayout_2.addWidget(self.group_url)

        self.group_request = GroupBox(self.editPlace_WidgetContents)
        self.group_request.setObjectName(u"group_request")
        self.verticalLayout_4 = QVBoxLayout(self.group_request)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.requestTopLayout = QHBoxLayout()
        self.requestTopLayout.setSpacing(10)
        self.requestTopLayout.setObjectName(u"request_top_layout")
        self.request_lable1 = QLabel(self.group_request)
        self.request_lable1.setObjectName(u"request_lable1")
        self.request_lable1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.requestTopLayout.addWidget(self.request_lable1)

        self.combo_requestMethod = ComboBox(self.group_request)
        self.combo_requestMethod.addItem("")
        self.combo_requestMethod.addItem("")
        self.combo_requestMethod.addItem("")
        self.combo_requestMethod.addItem("")
        self.combo_requestMethod.setObjectName(u"combo_request_method")

        self.requestTopLayout.addWidget(self.combo_requestMethod)

        self.request_lable3 = QLabel(self.group_request)
        self.request_lable3.setObjectName(u"request_lable3")

        self.requestTopLayout.addWidget(self.request_lable3)

        self.combo_responseEncoding = ComboBox(self.group_request)
        self.combo_responseEncoding.addItem("")
        self.combo_responseEncoding.setObjectName(u"combo_response_encoding")

        self.requestTopLayout.addWidget(self.combo_responseEncoding)

        self.request_lable4 = QLabel(self.group_request)
        self.request_lable4.setObjectName(u"request_lable4")

        self.requestTopLayout.addWidget(self.request_lable4)

        self.spin_requestTimeout = SpinBox(self.group_request)
        self.spin_requestTimeout.setObjectName(u"spin_request_timeout")
        self.spin_requestTimeout.setMinimumSize(QSize(60, 0))
        self.spin_requestTimeout.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_requestTimeout.setMaximum(600)

        self.requestTopLayout.addWidget(self.spin_requestTimeout)

        self.check_verify = QCheckBox(self.group_request)
        self.check_verify.setObjectName(u"check_verify")

        self.requestTopLayout.addWidget(self.check_verify)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.requestTopLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4.addLayout(self.requestTopLayout)

        self.group_headers = GroupBox(self.group_request)
        self.group_headers.setObjectName(u"group_headers")
        self.verticalLayout_9 = QVBoxLayout(self.group_headers)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.headersBtnLayout = QHBoxLayout()
        self.headersBtnLayout.setObjectName(u"headers_btn_layout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headersBtnLayout.addItem(self.horizontalSpacer_7)

        self.btn_headersParse = PushButton(self.group_headers)
        self.btn_headersParse.setObjectName(u"btn_headers_parse")

        self.headersBtnLayout.addWidget(self.btn_headersParse)

        self.btn_headersAdd = PushButton(self.group_headers)
        self.btn_headersAdd.setObjectName(u"btn_headers_add")

        self.headersBtnLayout.addWidget(self.btn_headersAdd)

        self.btn_headersDelete = PushButton(self.group_headers)
        self.btn_headersDelete.setObjectName(u"btn_headers_delete")

        self.headersBtnLayout.addWidget(self.btn_headersDelete)

        self.verticalLayout_9.addLayout(self.headersBtnLayout)

        self.table_headers = TableWidget(self.group_headers)
        self.table_headers.setObjectName(u"table_headers")

        self.verticalLayout_9.addWidget(self.table_headers)

        self.verticalLayout_4.addWidget(self.group_headers)

        self.requestFormLayout = QHBoxLayout()
        self.requestFormLayout.setObjectName(u"request_form_layout")
        self.group_dataForm = GroupBox(self.group_request)
        self.group_dataForm.setObjectName(u"group_data_form")
        self.group_dataForm.setCheckable(True)
        self.group_dataForm.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.group_dataForm)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.dataFormBtnLayout = QHBoxLayout()
        self.dataFormBtnLayout.setObjectName(u"data_form_btn_layout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dataFormBtnLayout.addItem(self.horizontalSpacer_5)

        self.btn_dataForm_add = PushButton(self.group_dataForm)
        self.btn_dataForm_add.setObjectName(u"btn_data_form_add")

        self.dataFormBtnLayout.addWidget(self.btn_dataForm_add)

        self.btn_dataForm_delete = PushButton(self.group_dataForm)
        self.btn_dataForm_delete.setObjectName(u"btn_data_form_delete")

        self.dataFormBtnLayout.addWidget(self.btn_dataForm_delete)

        self.verticalLayout_6.addLayout(self.dataFormBtnLayout)

        self.table_dataForm = TableWidget(self.group_dataForm)
        self.table_dataForm.setObjectName(u"table_data_form")
        self.table_dataForm.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.table_dataForm)

        self.requestFormLayout.addWidget(self.group_dataForm)

        self.group_dataForm_script = GroupBox(self.group_request)
        self.group_dataForm_script.setObjectName(u"group_data_form_script")
        self.group_dataForm_script.setCheckable(True)
        self.group_dataForm_script.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.group_dataForm_script)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.dataFormScriptBtnLayout = QHBoxLayout()
        self.dataFormScriptBtnLayout.setObjectName(u"data_form_script_btn_layout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dataFormScriptBtnLayout.addItem(self.horizontalSpacer_6)

        self.btn_dataForm_script_add = PushButton(self.group_dataForm_script)
        self.btn_dataForm_script_add.setObjectName(u"btn_data_form_script_add")

        self.dataFormScriptBtnLayout.addWidget(self.btn_dataForm_script_add)

        self.btn_dataForm_script_delete = PushButton(self.group_dataForm_script)
        self.btn_dataForm_script_delete.setObjectName(u"btn_data_form_script_delete")

        self.dataFormScriptBtnLayout.addWidget(self.btn_dataForm_script_delete)

        self.verticalLayout_7.addLayout(self.dataFormScriptBtnLayout)

        self.table_dataForm_script = TableWidget(self.group_dataForm_script)
        self.table_dataForm_script.setObjectName(u"table_data_form_script")
        self.table_dataForm_script.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.table_dataForm_script)

        self.requestFormLayout.addWidget(self.group_dataForm_script)

        self.verticalLayout_4.addLayout(self.requestFormLayout)

        self.group_cookies = GroupBox(self.group_request)
        self.group_cookies.setObjectName(u"group_cookies")
        self.verticalLayout_10 = QVBoxLayout(self.group_cookies)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.cookiesBtnLayout = QHBoxLayout()
        self.cookiesBtnLayout.setObjectName(u"cookies_btn_layout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cookiesBtnLayout.addItem(self.horizontalSpacer_8)

        self.btn_cookiesParse = PushButton(self.group_cookies)
        self.btn_cookiesParse.setObjectName(u"btn_cookies_parse")

        self.cookiesBtnLayout.addWidget(self.btn_cookiesParse)

        self.btn_cookiesAdd = PushButton(self.group_cookies)
        self.btn_cookiesAdd.setObjectName(u"btn_cookies_add")

        self.cookiesBtnLayout.addWidget(self.btn_cookiesAdd)

        self.btn_cookiesDelete = PushButton(self.group_cookies)
        self.btn_cookiesDelete.setObjectName(u"btn_cookies_delete")

        self.cookiesBtnLayout.addWidget(self.btn_cookiesDelete)

        self.verticalLayout_10.addLayout(self.cookiesBtnLayout)

        self.table_cookies = TableWidget(self.group_cookies)
        self.table_cookies.setObjectName(u"table_cookies")

        self.verticalLayout_10.addWidget(self.table_cookies)

        self.verticalLayout_4.addWidget(self.group_cookies)

        self.requestUaIpLayout = QHBoxLayout()
        self.requestUaIpLayout.setObjectName(u"request_ua_ip_layout")
        self.group_userAgentPool = GroupBox(self.group_request)
        self.group_userAgentPool.setObjectName(u"group_user_agent_pool")
        self.group_userAgentPool.setCheckable(True)
        self.group_userAgentPool.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.group_userAgentPool)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.tedit_userAgent = TextEdit(self.group_userAgentPool, heightScope=[80, 200], heightByDocument=True)
        self.tedit_userAgent.setObjectName(u"tedit_user_agent")
        self.tedit_userAgent.setLineWrapMode(TextEdit.NoWrap)

        self.verticalLayout_11.addWidget(self.tedit_userAgent)

        self.requestUaIpLayout.addWidget(self.group_userAgentPool)

        self.group_ipProxyPool = GroupBox(self.group_request)
        self.group_ipProxyPool.setObjectName(u"group_ip_proxy_pool")
        self.group_ipProxyPool.setCheckable(True)
        self.group_ipProxyPool.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.group_ipProxyPool)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.tedit_ipProxy = TextEdit(self.group_ipProxyPool, heightScope=[80, 200], heightByDocument=True)
        self.tedit_ipProxy.setObjectName(u"tedit_ip_proxy")
        self.tedit_ipProxy.setLineWrapMode(TextEdit.NoWrap)

        self.verticalLayout_12.addWidget(self.tedit_ipProxy)

        self.requestUaIpLayout.addWidget(self.group_ipProxyPool)

        self.verticalLayout_4.addLayout(self.requestUaIpLayout)

        self.verticalLayout_2.addWidget(self.group_request)

        self.group_parse = GroupBox(self.editPlace_WidgetContents)
        self.group_parse.setObjectName(u"group_parse")
        self.group_parse.setCheckable(True)
        self.group_parse.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.group_parse)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.parse_lable1 = QLabel(self.group_parse)
        self.parse_lable1.setObjectName(u"parse_lable1")

        self.horizontalLayout_4.addWidget(self.parse_lable1)

        self.combo_dataType = ComboBox(self.group_parse)
        self.combo_dataType.addItem("TEXT")
        self.combo_dataType.addItem("BIN")
        self.combo_dataType.setObjectName(u"combo_data_type")

        self.horizontalLayout_4.addWidget(self.combo_dataType)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.group_dataCut = GroupBox(self.group_parse)
        self.group_dataCut.setObjectName(u"group_data_cut")
        self.group_dataCut.setCheckable(True)
        self.group_dataCut.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.group_dataCut)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.dataCutTopLayout = QHBoxLayout()
        self.dataCutTopLayout.setObjectName(u"data_cut_top_layout")
        self.dataCut_label1 = QLabel(self.group_dataCut)
        self.dataCut_label1.setObjectName(u"data_cut_label1")

        self.dataCutTopLayout.addWidget(self.dataCut_label1)

        self.ledit_dataCut_tagName = LineEdit(self.group_dataCut)
        self.ledit_dataCut_tagName.setObjectName(u"ledit_data_cut_tag_name")

        self.dataCutTopLayout.addWidget(self.ledit_dataCut_tagName)

        self.verticalLayout_14.addLayout(self.dataCutTopLayout)

        self.dataCut_label2 = QLabel(self.group_dataCut)
        self.dataCut_label2.setObjectName(u"data_cut_label2")

        self.verticalLayout_14.addWidget(self.dataCut_label2)

        self.tedit_dataCut_attrs = TextEdit(self.group_dataCut, heightScope=[50, 150], heightByDocument=True)
        self.tedit_dataCut_attrs.setObjectName(u"tedit_data_cut_attrs")
        self.tedit_dataCut_attrs.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.tedit_dataCut_attrs)

        self.verticalLayout_13.addWidget(self.group_dataCut)

        self.group_parseSetting = GroupBox(self.group_parse)
        self.group_parseSetting.setObjectName(u"group_parse_setting")
        self.verticalLayout_15 = QVBoxLayout(self.group_parseSetting)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.psetPages = QStackedWidget(self.group_parseSetting)
        self.psetPages.setObjectName(u"pset_pages")
        self.psetTextPage = QWidget()
        self.psetTextPage.setObjectName(u"page_pset_text")
        self.verticalLayout_16 = QVBoxLayout(self.psetTextPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.psetTextPageBtnLayout = QHBoxLayout()
        self.psetTextPageBtnLayout.setObjectName(u"pset_text_btn_layout")
        self.pset_text_label1 = QLabel(self.psetTextPage)
        self.pset_text_label1.setObjectName(u"pset_text_label1")

        self.psetTextPageBtnLayout.addWidget(self.pset_text_label1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.psetTextPageBtnLayout.addItem(self.horizontalSpacer_10)

        self.btn_psetTextAdd = PushButton(self.psetTextPage)
        self.btn_psetTextAdd.setObjectName(u"btn_pset_text_add")

        self.psetTextPageBtnLayout.addWidget(self.btn_psetTextAdd)

        self.btn_psetTextDelete = PushButton(self.psetTextPage)
        self.btn_psetTextDelete.setObjectName(u"btn_pset_text_delete")

        self.psetTextPageBtnLayout.addWidget(self.btn_psetTextDelete)

        self.verticalLayout_16.addLayout(self.psetTextPageBtnLayout)

        self.table_psetText = TableWidget(self.psetTextPage, fixedColWidth=True)
        self.table_psetText.setObjectName(u"table_pset_text")

        self.verticalLayout_16.addWidget(self.table_psetText)

        self.psetPages.addWidget(self.psetTextPage)
        self.psetBinPage = QWidget()
        self.psetBinPage.setObjectName(u"page_pset_bin")
        self.verticalLayout_17 = QVBoxLayout(self.psetBinPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.psetBinPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame)

        self.psetPages.addWidget(self.psetBinPage)

        self.verticalLayout_15.addWidget(self.psetPages)

        self.verticalLayout_13.addWidget(self.group_parseSetting)

        self.verticalLayout_2.addWidget(self.group_parse)

        self.group_save = GroupBox(self.editPlace_WidgetContents)
        self.group_save.setObjectName(u"group_save")
        self.group_save.setCheckable(True)
        self.group_save.setChecked(False)
        self.verticalLayout_18 = QVBoxLayout(self.group_save)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dataSave_lable1 = QLabel(self.group_save)
        self.dataSave_lable1.setObjectName(u"data_save_lable1")

        self.horizontalLayout_3.addWidget(self.dataSave_lable1)

        self.combo_dataSavePath = ComboBox(self.group_save)
        self.combo_dataSavePath.addItem("")
        self.combo_dataSavePath.addItem("")
        self.combo_dataSavePath.setObjectName(u"combo_data_save_path")

        self.horizontalLayout_3.addWidget(self.combo_dataSavePath)

        self.ledit_dataSavePath = LineEdit(self.group_save)
        self.ledit_dataSavePath.setObjectName(u"ledit_data_save_path")

        self.horizontalLayout_3.addWidget(self.ledit_dataSavePath)

        self.btn_dataSavePath = PushButton(self.group_save)
        self.btn_dataSavePath.setObjectName(u"btn_data_save_path")

        self.horizontalLayout_3.addWidget(self.btn_dataSavePath)

        self.verticalLayout_18.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.group_saveText = GroupBox(self.group_save)
        self.group_saveText.setObjectName(u"group_save_text")
        self.formLayout_2 = QFormLayout(self.group_saveText)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.dataSave_lable2 = QLabel(self.group_saveText)
        self.dataSave_lable2.setObjectName(u"data_save_lable2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.dataSave_lable2)

        self.combo_saveText_fileType = ComboBox(self.group_saveText)
        self.combo_saveText_fileType.addItem("")
        self.combo_saveText_fileType.addItem("")
        self.combo_saveText_fileType.addItem("")
        self.combo_saveText_fileType.setObjectName(u"combo_save_text_file_type")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.combo_saveText_fileType)

        self.dataSave_lable3 = QLabel(self.group_saveText)
        self.dataSave_lable3.setObjectName(u"data_save_lable3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.dataSave_lable3)

        self.ledit_saveText_fileName = LineEdit(self.group_saveText)
        self.ledit_saveText_fileName.setObjectName(u"ledit_save_text_file_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ledit_saveText_fileName)

        self.check_saveText_paging = QCheckBox(self.group_saveText)
        self.check_saveText_paging.setObjectName(u"check_save_text_paging")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.check_saveText_paging)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer_11)

        self.dataSave_lable4 = QLabel(self.group_saveText)
        self.dataSave_lable4.setObjectName(u"data_save_lable4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.dataSave_lable4)

        self.spin_saveText_dataLimit = SpinBox(self.group_saveText)
        self.spin_saveText_dataLimit.setObjectName(u"spin_save_text_data_limit")
        self.spin_saveText_dataLimit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_saveText_dataLimit.setMinimum(1)
        self.spin_saveText_dataLimit.setMaximum(9999999)
        self.spin_saveText_dataLimit.setValue(1000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spin_saveText_dataLimit)

        self.horizontalLayout_5.addWidget(self.group_saveText)

        self.group_saveImage = GroupBox(self.group_save)
        self.group_saveImage.setObjectName(u"group_save_image")
        self.formLayout_3 = QFormLayout(self.group_saveImage)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.dataSave_lable5 = QLabel(self.group_saveImage)
        self.dataSave_lable5.setObjectName(u"data_save_lable5")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.dataSave_lable5)

        self.combo_saveImage_fileType = ComboBox(self.group_saveImage)
        self.combo_saveImage_fileType.addItem("")
        self.combo_saveImage_fileType.addItem("")
        self.combo_saveImage_fileType.setObjectName(u"combo_save_image_file_type")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.combo_saveImage_fileType)

        self.dataSave_lable6 = QLabel(self.group_saveImage)
        self.dataSave_lable6.setObjectName(u"data_save_lable6")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.dataSave_lable6)

        self.ledit_saveImage_fileName = LineEdit(self.group_saveImage)
        self.ledit_saveImage_fileName.setObjectName(u"ledit_save_image_file_name")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ledit_saveImage_fileName)

        self.horizontalLayout_5.addWidget(self.group_saveImage)

        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.addWidget(self.group_save)

        self.editPlace.setWidget(self.editPlace_WidgetContents)

        self.verticalLayout.addWidget(self.editPlace)

        self.retranslateUi(ConfigurationEditor)

        QMetaObject.connectSlotsByName(ConfigurationEditor)

    # setupUi

    def retranslateUi(self, ConfigurationEditor):
        ConfigurationEditor.setWindowTitle(QCoreApplication.translate("ConfigurationEditor", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8fd4\u56de", None))
        self.btn_editInJson.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5728Json\u6587\u4ef6\u4e2d\u7f16\u8f91", None))
        self.btn_save.setText(QCoreApplication.translate("ConfigurationEditor", u"\u4fdd\u5b58", None))
        self.group_url.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u8bbe\u7f6e", None))
        self.urlSet_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u6765\u6e90", None))
        self.combo_urlSource.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"\u624b\u52a8\u7f16\u8f91", None))
        self.combo_urlSource.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"\u6587\u4ef6\u5bfc\u5165", None))

        self.btn_urlSetConfirm.setText(QCoreApplication.translate("ConfigurationEditor", u"\u786e\u8ba4", None))
        self.group_parameter.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u53c2\u6570", None))
        self.btn_parameterAdd.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_parameterDelete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_iteration.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8fed\u4ee3\u53c2\u6570", None))
        self.iteration_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u53c2\u6570\u540d\u79f0", None))
        self.iteration_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8d77\u59cb\u503c", None))
        self.iteration_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7ed3\u675f\u503c", None))
        self.iteration_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6b65\u957f", None))
        self.urlView_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7f16\u8f91\u548c\u9884\u89c8", None))
        self.urlView_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u603b\u6761\u6570", None))
        self.btn_urlView_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_urlView_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_request.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u7f51\u7edc\u8bf7\u6c42\u4e0e\u54cd\u5e94\u8bbe\u7f6e", None))
        self.request_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u65b9\u5f0f", None))
        self.combo_requestMethod.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"GET", None))
        self.combo_requestMethod.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"POST", None))
        self.combo_requestMethod.setItemText(2, QCoreApplication.translate("ConfigurationEditor", u"PUT", None))
        self.combo_requestMethod.setItemText(3, QCoreApplication.translate("ConfigurationEditor", u"DELETE", None))

        self.request_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u54cd\u5e94\u6570\u636e\u7f16\u7801", None))
        self.combo_responseEncoding.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"UTF-8", None))

        self.request_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.check_verify.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8bc1\u4e66\u9a8c\u8bc1", None))
        self.group_headers.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u5934", None))
        self.btn_headersParse.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7c98\u8d34", None))
        self.btn_headersAdd.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_headersDelete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_dataForm.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u6570\u636e\u8868\u5355(\u76f4\u63a5\u586b\u5199)", None))
        self.btn_dataForm_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_dataForm_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_dataForm_script.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u6570\u636e\u8868\u5355(\u811a\u672c\u751f\u6210)", None))
        self.btn_dataForm_script_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_dataForm_script_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_cookies.setTitle(QCoreApplication.translate("ConfigurationEditor", u"Cookies", None))
        self.btn_cookiesParse.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7c98\u8d34", None))
        self.btn_cookiesAdd.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_cookiesDelete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_userAgentPool.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u7528\u6237\u4ee3\u7406\u6c60", None))
        self.group_ipProxyPool.setTitle(QCoreApplication.translate("ConfigurationEditor", u"IP\u4ee3\u7406\u6c60", None))
        self.group_parse.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u89e3\u6790", None))
        self.parse_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u7c7b\u578b", None))

        self.group_dataCut.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u54cd\u5e94\u6570\u636e\u5207\u5206", None))
        self.dataCut_label1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6807\u7b7e\u540d\u79f0", None))
        self.dataCut_label2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6807\u7b7e\u5c5e\u6027", None))
        self.group_parseSetting.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u89e3\u6790\u8bbe\u7f6e", None))
        self.pset_text_label1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u7c7b\u578b: \u6587\u672c", None))
        self.btn_psetTextAdd.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_psetTextDelete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_save.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u5b58\u50a8", None))
        self.dataSave_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.combo_dataSavePath.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"\u8ddf\u968f\u8bbe\u7f6e", None))
        self.combo_dataSavePath.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"\u81ea\u5b9a\u4e49", None))

        self.btn_dataSavePath.setText(QCoreApplication.translate("ConfigurationEditor", u"\u9009\u62e9\u4f4d\u7f6e", None))
        self.group_saveText.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6587\u672c\u6570\u636e", None))
        self.dataSave_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u7c7b\u578b", None))
        self.combo_saveText_fileType.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"TXT", None))
        self.combo_saveText_fileType.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"EXCEL", None))
        self.combo_saveText_fileType.setItemText(2, QCoreApplication.translate("ConfigurationEditor", u"SQL", None))

        self.dataSave_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u540d\u79f0", None))
        self.check_saveText_paging.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u5206\u9875", None))
        self.dataSave_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5355\u9875\u6570\u636e\u4e0a\u9650", None))
        self.group_saveImage.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u4e8c\u8fdb\u5236-\u56fe\u7247", None))
        self.dataSave_lable5.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u7c7b\u578b", None))
        self.combo_saveImage_fileType.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"JPG", None))
        self.combo_saveImage_fileType.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"PNG", None))

        self.dataSave_lable6.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u540d\u79f0", None))

    # retranslateUi
