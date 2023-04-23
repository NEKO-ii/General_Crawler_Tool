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

from core.sys import Themes
from ui.widgets import (ComboBox, LineEdit, List, PushButton, ScrollArea, SpinBox, TableWidget, TextEdit, GroupBox)


class Ui_ConfigurationEditor(object):

    def __init__(self, ConfigurationEditor: QWidget, themes: Themes) -> None:
        self.style = F'''
        #edit_place_WidgetContents {{
            background-color: {themes.color["bg_1"]};
            border: 1px solid {themes.color["dark_3"]};
        }}
        #line {{
            background-color: {themes.color["bg_3"]};
        }}
        QLabel:enabled {{
            color: {themes.color["text_foreground"]};
        }}
        QLabel:disabled {{
            color: {themes.color["text_description"]};
        }}
        '''
        self.setupUi(ConfigurationEditor, themes)
        ConfigurationEditor.setStyleSheet(self.style)
        self.set_scroll_parent(ConfigurationEditor)
        self.set_tableHeader()

    def set_scroll_parent(self, ConfigurationEditor: QWidget) -> None:
        for item in ConfigurationEditor.findChildren(QComboBox):
            item.set_scroll_parent(self.edit_place)
        for item in ConfigurationEditor.findChildren(QTextEdit):
            item.set_scroll_parent(self.edit_place)
        for item in ConfigurationEditor.findChildren(QSpinBox):
            item.set_scroll_parent(self.edit_place)
        for item in ConfigurationEditor.findChildren(QListWidget):
            item.set_scroll_parent(self.edit_place)
        for item in ConfigurationEditor.findChildren(QTableWidget):
            item.set_scroll_parent(self.edit_place)

    def set_tableHeader(self) -> None:
        self.table_parameter.set_header(["参数名", "参数值"])
        self.table_headers.set_header(["参数名", "参数值"])
        self.table_headers.setColumnWidth(0, 200)
        self.table_data_form.set_header(["参数名", "参数值"])
        self.table_data_form_script.set_header(["参数名", "来源模块", "输入参数", "输出列表索引"])
        self.table_data_form_script.set_header_tooltip([None, "该参数名对应的值由哪个模块输出\n输入模块名(需要后缀)", "若该模块需要输入参数则在此填写\n若不需要则留空", "若该模块输出一个列表而参数值只需要其中一项\n在此处输入该项的索引(起始为1)"])
        self.table_cookies.set_header(["键", "值"])
        self.table_cookies.setColumnWidth(0, 200)
        self.table_pset_text.set_header(["方法", "匹配语法", "索引值", "间隔字符"])
        self.table_pset_text.set_col_width([120, 700, 200])
        self.table_pset_text.set_header_tooltip(["文本匹配方式\nRE:正则表达式匹配\nBS4:BeautifulSoup标签搜索语法\nXPATH:XML路径定位语法", "所选方法对应的匹配语句", "若前面的语法匹配到的结果不止一个\n可在此填写所需结果的索引\n(起始为0,空表示选择所有,可多选索引间用逗号分隔)", "若有多个匹配结果,可在此填写多个结果间的分隔符\n默认为空代表空格"])

    def setupUi(self, ConfigurationEditor: QWidget, themes: Themes):
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
        self.top_bar = QFrame(ConfigurationEditor)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_back = PushButton(self.top_bar)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_2.addWidget(self.btn_back)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btn_default = PushButton(self.top_bar, text="恢复默认", type="warning")
        self.btn_default.setObjectName(u"btn_default")
        self.horizontalLayout_2.addWidget(self.btn_default)

        self.btn_edit_json = PushButton(self.top_bar, type="primary")
        self.btn_edit_json.setObjectName(u"btn_edit_json")
        self.horizontalLayout_2.addWidget(self.btn_edit_json)

        self.btn_save = PushButton(self.top_bar, type="success")
        self.btn_save.setObjectName(u"btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)

        self.verticalLayout.addWidget(self.top_bar)

        self.edit_place = ScrollArea(ConfigurationEditor)
        self.edit_place.setObjectName(u"edit_place")
        self.edit_place.setWidgetResizable(True)
        self.edit_place_WidgetContents = QWidget()
        self.edit_place_WidgetContents.setObjectName(u"edit_place_WidgetContents")
        self.edit_place_WidgetContents.setGeometry(QRect(0, 0, 887, 1375))
        self.verticalLayout_2 = QVBoxLayout(self.edit_place_WidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.group_url = GroupBox(self.edit_place_WidgetContents)
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
        self.url_set = QFrame(self.group_url)
        self.url_set.setObjectName(u"url_set")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.url_set.sizePolicy().hasHeightForWidth())
        self.url_set.setSizePolicy(sizePolicy1)
        self.url_set.setMinimumSize(QSize(0, 0))
        self.url_set.setMaximumSize(QSize(16777215, 16777215))
        self.url_set.setFrameShape(QFrame.StyledPanel)
        self.url_set.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.url_set)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.url_set_top_layout = QHBoxLayout()
        self.url_set_top_layout.setObjectName(u"url_set_top_layout")
        self.url_set_lable1 = QLabel(self.url_set)
        self.url_set_lable1.setObjectName(u"url_set_lable1")

        self.url_set_top_layout.addWidget(self.url_set_lable1)

        self.combo_url_source = ComboBox(self.url_set)
        self.combo_url_source.addItem("")
        self.combo_url_source.addItem("")
        self.combo_url_source.setObjectName(u"combo_url_source")

        self.url_set_top_layout.addWidget(self.combo_url_source)

        self.ledit_url_source = LineEdit(self.url_set, place_holder_text="输入网址基本路径")
        self.ledit_url_source.setObjectName(u"ledit_url_source")

        self.url_set_top_layout.addWidget(self.ledit_url_source)

        self.btn_choose_file = PushButton(self.url_set, "文件")
        self.btn_choose_file.setEnabled(False)
        self.btn_choose_file.setObjectName(u"btn_choose_file")
        self.url_set_top_layout.addWidget(self.btn_choose_file)

        self.btn_url_set_confirm = PushButton(self.url_set, type="primary")
        self.btn_url_set_confirm.setObjectName(u"btn_url_set_confirm")

        self.url_set_top_layout.addWidget(self.btn_url_set_confirm)

        self.verticalLayout_8.addLayout(self.url_set_top_layout)

        self.url_set_bottom_layout = QHBoxLayout()
        self.url_set_bottom_layout.setObjectName(u"url_set_bottom_layout")
        self.group_parameter = GroupBox(self.url_set)
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
        self.parameter_btn_layout = QHBoxLayout()
        self.parameter_btn_layout.setObjectName(u"parameter_btn_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.parameter_btn_layout.addItem(self.horizontalSpacer_2)

        self.btn_parameter_add = PushButton(self.group_parameter)
        self.btn_parameter_add.setObjectName(u"btn_parameter_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_parameter_add.sizePolicy().hasHeightForWidth())
        self.btn_parameter_add.setSizePolicy(sizePolicy2)
        self.btn_parameter_add.setMaximumSize(QSize(16777215, 16777215))

        self.parameter_btn_layout.addWidget(self.btn_parameter_add)

        self.btn_parameter_delete = PushButton(self.group_parameter)
        self.btn_parameter_delete.setObjectName(u"btn_parameter_delete")
        self.btn_parameter_delete.setMaximumSize(QSize(16777215, 16777215))

        self.parameter_btn_layout.addWidget(self.btn_parameter_delete)

        self.verticalLayout_5.addLayout(self.parameter_btn_layout)

        self.table_parameter = TableWidget(self.group_parameter)
        self.table_parameter.setObjectName(u"table_parameter")
        self.table_parameter.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.table_parameter)

        self.url_set_bottom_layout.addWidget(self.group_parameter)

        self.group_iteration = GroupBox(self.url_set)
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

        self.ledit_iteration_name = LineEdit(self.group_iteration)
        self.ledit_iteration_name.setObjectName(u"ledit_iteration_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledit_iteration_name)

        self.iteration_lable2 = QLabel(self.group_iteration)
        self.iteration_lable2.setObjectName(u"iteration_lable2")
        self.iteration_lable2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.iteration_lable2)

        self.ledit_iteration_start = LineEdit(self.group_iteration)
        self.ledit_iteration_start.setObjectName(u"ledit_iteration_start")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledit_iteration_start)

        self.iteration_lable3 = QLabel(self.group_iteration)
        self.iteration_lable3.setObjectName(u"iteration_lable3")
        self.iteration_lable3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.iteration_lable3)

        self.ledit_iteration_stop = LineEdit(self.group_iteration)
        self.ledit_iteration_stop.setObjectName(u"ledit_iteration_stop")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ledit_iteration_stop)

        self.iteration_lable4 = QLabel(self.group_iteration)
        self.iteration_lable4.setObjectName(u"iteration_lable4")
        self.iteration_lable4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.iteration_lable4)

        self.ledit_iteration_step = LineEdit(self.group_iteration)
        self.ledit_iteration_step.setObjectName(u"ledit_iteration_step")
        self.ledit_iteration_step.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ledit_iteration_step)

        self.url_set_bottom_layout.addWidget(self.group_iteration)

        self.verticalLayout_8.addLayout(self.url_set_bottom_layout)

        self.horizontalLayout.addWidget(self.url_set)

        self.line = QFrame(self.group_url)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.url_view = QFrame(self.group_url)
        self.url_view.setObjectName(u"url_view")
        self.url_view.setFrameShape(QFrame.StyledPanel)
        self.url_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.url_view)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.url_view_top_layout = QHBoxLayout()
        self.url_view_top_layout.setObjectName(u"url_view_top_layout")
        self.url_view_lable1 = QLabel(self.url_view)
        self.url_view_lable1.setObjectName(u"url_view_lable1")

        self.url_view_top_layout.addWidget(self.url_view_lable1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.url_view_top_layout.addItem(self.horizontalSpacer)

        self.url_view_lable2 = QLabel(self.url_view)
        self.url_view_lable2.setObjectName(u"url_view_lable2")
        self.url_view_lable2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.url_view_top_layout.addWidget(self.url_view_lable2)

        self.ledit_url_view_count = LineEdit(self.url_view, color_enabled="rgb(17, 169, 225)")
        self.ledit_url_view_count.setObjectName(u"ledit_url_view_count")
        self.ledit_url_view_count.setEnabled(True)
        self.ledit_url_view_count.setMinimumSize(QSize(60, 0))
        self.ledit_url_view_count.setMaximumSize(QSize(60, 16777215))
        self.ledit_url_view_count.setReadOnly(True)
        self.ledit_url_view_count.setFocusPolicy(Qt.NoFocus)

        self.url_view_top_layout.addWidget(self.ledit_url_view_count)

        self.btn_url_view_add = PushButton(self.url_view)
        self.btn_url_view_add.setObjectName(u"btn_url_view_add")
        self.btn_url_view_add.setMaximumSize(QSize(70, 16777215))

        self.url_view_top_layout.addWidget(self.btn_url_view_add)

        self.btn_url_view_delete = PushButton(self.url_view)
        self.btn_url_view_delete.setObjectName(u"btn_url_view_delete")
        self.btn_url_view_delete.setMaximumSize(QSize(70, 16777215))

        self.url_view_top_layout.addWidget(self.btn_url_view_delete)

        self.verticalLayout_3.addLayout(self.url_view_top_layout)

        self.list_url_view = List(self.url_view)
        self.list_url_view.setObjectName(u"list_url_view")
        self.list_url_view.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.list_url_view)

        self.horizontalLayout.addWidget(self.url_view)

        self.verticalLayout_2.addWidget(self.group_url)

        self.group_request = GroupBox(self.edit_place_WidgetContents)
        self.group_request.setObjectName(u"group_request")
        self.verticalLayout_4 = QVBoxLayout(self.group_request)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.request_top_layout = QHBoxLayout()
        self.request_top_layout.setSpacing(10)
        self.request_top_layout.setObjectName(u"request_top_layout")
        self.request_lable1 = QLabel(self.group_request)
        self.request_lable1.setObjectName(u"request_lable1")
        self.request_lable1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.request_top_layout.addWidget(self.request_lable1)

        self.combo_request_method = ComboBox(self.group_request)
        self.combo_request_method.addItem("")
        self.combo_request_method.addItem("")
        self.combo_request_method.addItem("")
        self.combo_request_method.addItem("")
        self.combo_request_method.setObjectName(u"combo_request_method")

        self.request_top_layout.addWidget(self.combo_request_method)

        self.request_lable3 = QLabel(self.group_request)
        self.request_lable3.setObjectName(u"request_lable3")

        self.request_top_layout.addWidget(self.request_lable3)

        self.combo_response_encoding = ComboBox(self.group_request)
        self.combo_response_encoding.addItem("")
        self.combo_response_encoding.setObjectName(u"combo_response_encoding")

        self.request_top_layout.addWidget(self.combo_response_encoding)

        self.request_lable4 = QLabel(self.group_request)
        self.request_lable4.setObjectName(u"request_lable4")

        self.request_top_layout.addWidget(self.request_lable4)

        self.spin_request_timeout = SpinBox(self.group_request)
        self.spin_request_timeout.setObjectName(u"spin_request_timeout")
        self.spin_request_timeout.setMinimumSize(QSize(60, 0))
        self.spin_request_timeout.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_request_timeout.setMaximum(600)

        self.request_top_layout.addWidget(self.spin_request_timeout)

        self.check_verify = QCheckBox(self.group_request)
        self.check_verify.setObjectName(u"check_verify")

        self.request_top_layout.addWidget(self.check_verify)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.request_top_layout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4.addLayout(self.request_top_layout)

        self.group_headers = GroupBox(self.group_request)
        self.group_headers.setObjectName(u"group_headers")
        self.verticalLayout_9 = QVBoxLayout(self.group_headers)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.headers_btn_layout = QHBoxLayout()
        self.headers_btn_layout.setObjectName(u"headers_btn_layout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headers_btn_layout.addItem(self.horizontalSpacer_7)

        self.btn_headers_parse = PushButton(self.group_headers)
        self.btn_headers_parse.setObjectName(u"btn_headers_parse")

        self.headers_btn_layout.addWidget(self.btn_headers_parse)

        self.btn_headers_add = PushButton(self.group_headers)
        self.btn_headers_add.setObjectName(u"btn_headers_add")

        self.headers_btn_layout.addWidget(self.btn_headers_add)

        self.btn_headers_delete = PushButton(self.group_headers)
        self.btn_headers_delete.setObjectName(u"btn_headers_delete")

        self.headers_btn_layout.addWidget(self.btn_headers_delete)

        self.verticalLayout_9.addLayout(self.headers_btn_layout)

        self.table_headers = TableWidget(self.group_headers)
        self.table_headers.setObjectName(u"table_headers")

        self.verticalLayout_9.addWidget(self.table_headers)

        self.verticalLayout_4.addWidget(self.group_headers)

        self.request_form_layout = QHBoxLayout()
        self.request_form_layout.setObjectName(u"request_form_layout")
        self.group_data_form = GroupBox(self.group_request)
        self.group_data_form.setObjectName(u"group_data_form")
        self.group_data_form.setCheckable(True)
        self.group_data_form.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.group_data_form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.data_form_btn_layout = QHBoxLayout()
        self.data_form_btn_layout.setObjectName(u"data_form_btn_layout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.data_form_btn_layout.addItem(self.horizontalSpacer_5)

        self.btn_data_form_add = PushButton(self.group_data_form)
        self.btn_data_form_add.setObjectName(u"btn_data_form_add")

        self.data_form_btn_layout.addWidget(self.btn_data_form_add)

        self.btn_data_form_delete = PushButton(self.group_data_form)
        self.btn_data_form_delete.setObjectName(u"btn_data_form_delete")

        self.data_form_btn_layout.addWidget(self.btn_data_form_delete)

        self.verticalLayout_6.addLayout(self.data_form_btn_layout)

        self.table_data_form = TableWidget(self.group_data_form)
        self.table_data_form.setObjectName(u"table_data_form")
        self.table_data_form.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.table_data_form)

        self.request_form_layout.addWidget(self.group_data_form)

        self.group_data_form_script = GroupBox(self.group_request)
        self.group_data_form_script.setObjectName(u"group_data_form_script")
        self.group_data_form_script.setCheckable(True)
        self.group_data_form_script.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.group_data_form_script)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.data_form_script_btn_layout = QHBoxLayout()
        self.data_form_script_btn_layout.setObjectName(u"data_form_script_btn_layout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.data_form_script_btn_layout.addItem(self.horizontalSpacer_6)

        self.btn_data_form_script_add = PushButton(self.group_data_form_script)
        self.btn_data_form_script_add.setObjectName(u"btn_data_form_script_add")

        self.data_form_script_btn_layout.addWidget(self.btn_data_form_script_add)

        self.btn_data_form_script_delete = PushButton(self.group_data_form_script)
        self.btn_data_form_script_delete.setObjectName(u"btn_data_form_script_delete")

        self.data_form_script_btn_layout.addWidget(self.btn_data_form_script_delete)

        self.verticalLayout_7.addLayout(self.data_form_script_btn_layout)

        self.table_data_form_script = TableWidget(self.group_data_form_script)
        self.table_data_form_script.setObjectName(u"table_data_form_script")
        self.table_data_form_script.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.table_data_form_script)

        self.request_form_layout.addWidget(self.group_data_form_script)

        self.verticalLayout_4.addLayout(self.request_form_layout)

        self.group_cookies = GroupBox(self.group_request)
        self.group_cookies.setObjectName(u"group_cookies")
        self.verticalLayout_10 = QVBoxLayout(self.group_cookies)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.cookies_btn_layout = QHBoxLayout()
        self.cookies_btn_layout.setObjectName(u"cookies_btn_layout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cookies_btn_layout.addItem(self.horizontalSpacer_8)

        self.btn_cookies_parse = PushButton(self.group_cookies)
        self.btn_cookies_parse.setObjectName(u"btn_cookies_parse")

        self.cookies_btn_layout.addWidget(self.btn_cookies_parse)

        self.btn_cookies_add = PushButton(self.group_cookies)
        self.btn_cookies_add.setObjectName(u"btn_cookies_add")

        self.cookies_btn_layout.addWidget(self.btn_cookies_add)

        self.btn_cookies_delete = PushButton(self.group_cookies)
        self.btn_cookies_delete.setObjectName(u"btn_cookies_delete")

        self.cookies_btn_layout.addWidget(self.btn_cookies_delete)

        self.verticalLayout_10.addLayout(self.cookies_btn_layout)

        self.table_cookies = TableWidget(self.group_cookies)
        self.table_cookies.setObjectName(u"table_cookies")

        self.verticalLayout_10.addWidget(self.table_cookies)

        self.verticalLayout_4.addWidget(self.group_cookies)

        self.request_ua_ip_layout = QHBoxLayout()
        self.request_ua_ip_layout.setObjectName(u"request_ua_ip_layout")
        self.group_user_agent_pool = GroupBox(self.group_request)
        self.group_user_agent_pool.setObjectName(u"group_user_agent_pool")
        self.group_user_agent_pool.setCheckable(True)
        self.group_user_agent_pool.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.group_user_agent_pool)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.tedit_user_agent = TextEdit(self.group_user_agent_pool, max_height=150)
        self.tedit_user_agent.setObjectName(u"tedit_user_agent")
        self.tedit_user_agent.setMinimumSize(QSize(0, 0))
        self.tedit_user_agent.setLineWrapMode(TextEdit.NoWrap)

        self.verticalLayout_11.addWidget(self.tedit_user_agent)

        self.request_ua_ip_layout.addWidget(self.group_user_agent_pool)

        self.group_ip_proxy_pool = GroupBox(self.group_request)
        self.group_ip_proxy_pool.setObjectName(u"group_ip_proxy_pool")
        self.group_ip_proxy_pool.setCheckable(True)
        self.group_ip_proxy_pool.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.group_ip_proxy_pool)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.tedit_ip_proxy = TextEdit(self.group_ip_proxy_pool, max_height=150)
        self.tedit_ip_proxy.setObjectName(u"tedit_ip_proxy")
        self.tedit_ip_proxy.setMinimumSize(QSize(0, 0))
        self.tedit_ip_proxy.setLineWrapMode(TextEdit.NoWrap)

        self.verticalLayout_12.addWidget(self.tedit_ip_proxy)

        self.request_ua_ip_layout.addWidget(self.group_ip_proxy_pool)

        self.verticalLayout_4.addLayout(self.request_ua_ip_layout)

        self.verticalLayout_2.addWidget(self.group_request)

        self.group_parse = GroupBox(self.edit_place_WidgetContents)
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

        self.combo_data_type = ComboBox(self.group_parse)
        self.combo_data_type.addItem("TEXT")
        self.combo_data_type.addItem("BIN")
        self.combo_data_type.setObjectName(u"combo_data_type")

        self.horizontalLayout_4.addWidget(self.combo_data_type)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.group_data_cut = GroupBox(self.group_parse)
        self.group_data_cut.setObjectName(u"group_data_cut")
        self.group_data_cut.setCheckable(True)
        self.group_data_cut.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.group_data_cut)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.data_cut_top_layout = QHBoxLayout()
        self.data_cut_top_layout.setObjectName(u"data_cut_top_layout")
        self.data_cut_label1 = QLabel(self.group_data_cut)
        self.data_cut_label1.setObjectName(u"data_cut_label1")

        self.data_cut_top_layout.addWidget(self.data_cut_label1)

        self.ledit_data_cut_tag_name = LineEdit(self.group_data_cut)
        self.ledit_data_cut_tag_name.setObjectName(u"ledit_data_cut_tag_name")

        self.data_cut_top_layout.addWidget(self.ledit_data_cut_tag_name)

        self.verticalLayout_14.addLayout(self.data_cut_top_layout)

        self.data_cut_label2 = QLabel(self.group_data_cut)
        self.data_cut_label2.setObjectName(u"data_cut_label2")

        self.verticalLayout_14.addWidget(self.data_cut_label2)

        self.tedit_data_cut_attrs = TextEdit(self.group_data_cut, max_height=150)
        self.tedit_data_cut_attrs.setObjectName(u"tedit_data_cut_attrs")
        self.tedit_data_cut_attrs.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.tedit_data_cut_attrs)

        self.verticalLayout_13.addWidget(self.group_data_cut)

        self.group_parse_setting = GroupBox(self.group_parse)
        self.group_parse_setting.setObjectName(u"group_parse_setting")
        self.verticalLayout_15 = QVBoxLayout(self.group_parse_setting)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.pset_pages = QStackedWidget(self.group_parse_setting)
        self.pset_pages.setObjectName(u"pset_pages")
        self.page_pset_text = QWidget()
        self.page_pset_text.setObjectName(u"page_pset_text")
        self.verticalLayout_16 = QVBoxLayout(self.page_pset_text)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.pset_text_btn_layout = QHBoxLayout()
        self.pset_text_btn_layout.setObjectName(u"pset_text_btn_layout")
        self.pset_text_label1 = QLabel(self.page_pset_text)
        self.pset_text_label1.setObjectName(u"pset_text_label1")

        self.pset_text_btn_layout.addWidget(self.pset_text_label1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pset_text_btn_layout.addItem(self.horizontalSpacer_10)

        self.btn_pset_text_add = PushButton(self.page_pset_text)
        self.btn_pset_text_add.setObjectName(u"btn_pset_text_add")

        self.pset_text_btn_layout.addWidget(self.btn_pset_text_add)

        self.btn_pset_text_delete = PushButton(self.page_pset_text)
        self.btn_pset_text_delete.setObjectName(u"btn_pset_text_delete")

        self.pset_text_btn_layout.addWidget(self.btn_pset_text_delete)

        self.verticalLayout_16.addLayout(self.pset_text_btn_layout)

        self.table_pset_text = TableWidget(self.page_pset_text, fixed_col_width=True)
        self.table_pset_text.setObjectName(u"table_pset_text")

        self.verticalLayout_16.addWidget(self.table_pset_text)

        self.pset_pages.addWidget(self.page_pset_text)
        self.page_pset_image = QWidget()
        self.page_pset_image.setObjectName(u"page_pset_image")
        self.verticalLayout_17 = QVBoxLayout(self.page_pset_image)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.page_pset_image)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame)

        self.pset_pages.addWidget(self.page_pset_image)

        self.verticalLayout_15.addWidget(self.pset_pages)

        self.verticalLayout_13.addWidget(self.group_parse_setting)

        self.verticalLayout_2.addWidget(self.group_parse)

        self.group_save = GroupBox(self.edit_place_WidgetContents)
        self.group_save.setObjectName(u"group_save")
        self.group_save.setCheckable(True)
        self.group_save.setChecked(False)
        self.verticalLayout_18 = QVBoxLayout(self.group_save)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.data_save_lable1 = QLabel(self.group_save)
        self.data_save_lable1.setObjectName(u"data_save_lable1")

        self.horizontalLayout_3.addWidget(self.data_save_lable1)

        self.combo_data_save_path = ComboBox(self.group_save)
        self.combo_data_save_path.addItem("")
        self.combo_data_save_path.addItem("")
        self.combo_data_save_path.setObjectName(u"combo_data_save_path")

        self.horizontalLayout_3.addWidget(self.combo_data_save_path)

        self.ledit_data_save_path = LineEdit(self.group_save)
        self.ledit_data_save_path.setObjectName(u"ledit_data_save_path")

        self.horizontalLayout_3.addWidget(self.ledit_data_save_path)

        self.btn_data_save_path = PushButton(self.group_save)
        self.btn_data_save_path.setObjectName(u"btn_data_save_path")

        self.horizontalLayout_3.addWidget(self.btn_data_save_path)

        self.verticalLayout_18.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.group_save_text = GroupBox(self.group_save)
        self.group_save_text.setObjectName(u"group_save_text")
        self.formLayout_2 = QFormLayout(self.group_save_text)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.data_save_lable2 = QLabel(self.group_save_text)
        self.data_save_lable2.setObjectName(u"data_save_lable2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.data_save_lable2)

        self.combo_save_text_file_type = ComboBox(self.group_save_text)
        self.combo_save_text_file_type.addItem("")
        self.combo_save_text_file_type.addItem("")
        self.combo_save_text_file_type.addItem("")
        self.combo_save_text_file_type.setObjectName(u"combo_save_text_file_type")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.combo_save_text_file_type)

        self.data_save_lable3 = QLabel(self.group_save_text)
        self.data_save_lable3.setObjectName(u"data_save_lable3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.data_save_lable3)

        self.ledit_save_text_file_name = LineEdit(self.group_save_text)
        self.ledit_save_text_file_name.setObjectName(u"ledit_save_text_file_name")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ledit_save_text_file_name)

        self.check_save_text_paging = QCheckBox(self.group_save_text)
        self.check_save_text_paging.setObjectName(u"check_save_text_paging")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.check_save_text_paging)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer_11)

        self.data_save_lable4 = QLabel(self.group_save_text)
        self.data_save_lable4.setObjectName(u"data_save_lable4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.data_save_lable4)

        self.spin_save_text_data_limit = SpinBox(self.group_save_text)
        self.spin_save_text_data_limit.setObjectName(u"spin_save_text_data_limit")
        self.spin_save_text_data_limit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_save_text_data_limit.setMinimum(1)
        self.spin_save_text_data_limit.setMaximum(9999999)
        self.spin_save_text_data_limit.setValue(1000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spin_save_text_data_limit)

        self.horizontalLayout_5.addWidget(self.group_save_text)

        self.group_save_image = GroupBox(self.group_save)
        self.group_save_image.setObjectName(u"group_save_image")
        self.formLayout_3 = QFormLayout(self.group_save_image)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.data_save_lable5 = QLabel(self.group_save_image)
        self.data_save_lable5.setObjectName(u"data_save_lable5")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.data_save_lable5)

        self.combo_save_image_file_type = ComboBox(self.group_save_image)
        self.combo_save_image_file_type.addItem("")
        self.combo_save_image_file_type.addItem("")
        self.combo_save_image_file_type.setObjectName(u"combo_save_image_file_type")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.combo_save_image_file_type)

        self.data_save_lable6 = QLabel(self.group_save_image)
        self.data_save_lable6.setObjectName(u"data_save_lable6")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.data_save_lable6)

        self.ledit_save_image_file_name = LineEdit(self.group_save_image)
        self.ledit_save_image_file_name.setObjectName(u"ledit_save_image_file_name")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ledit_save_image_file_name)

        self.horizontalLayout_5.addWidget(self.group_save_image)

        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.addWidget(self.group_save)

        self.edit_place.setWidget(self.edit_place_WidgetContents)

        self.verticalLayout.addWidget(self.edit_place)

        self.retranslateUi(ConfigurationEditor)

        QMetaObject.connectSlotsByName(ConfigurationEditor)

    # setupUi

    def retranslateUi(self, ConfigurationEditor):
        ConfigurationEditor.setWindowTitle(QCoreApplication.translate("ConfigurationEditor", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8fd4\u56de", None))
        self.btn_edit_json.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5728Json\u6587\u4ef6\u4e2d\u7f16\u8f91", None))
        self.btn_save.setText(QCoreApplication.translate("ConfigurationEditor", u"\u4fdd\u5b58", None))
        self.group_url.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u8bbe\u7f6e", None))
        self.url_set_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u6765\u6e90", None))
        self.combo_url_source.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"\u624b\u52a8\u7f16\u8f91", None))
        self.combo_url_source.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"\u6587\u4ef6\u5bfc\u5165", None))

        self.btn_url_set_confirm.setText(QCoreApplication.translate("ConfigurationEditor", u"\u786e\u8ba4", None))
        self.group_parameter.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u5730\u5740\u53c2\u6570", None))
        self.btn_parameter_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_parameter_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_iteration.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8fed\u4ee3\u53c2\u6570", None))
        self.iteration_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u53c2\u6570\u540d\u79f0", None))
        self.iteration_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8d77\u59cb\u503c", None))
        self.iteration_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7ed3\u675f\u503c", None))
        self.iteration_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6b65\u957f", None))
        self.url_view_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7f16\u8f91\u548c\u9884\u89c8", None))
        self.url_view_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u603b\u6761\u6570", None))
        self.btn_url_view_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_url_view_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_request.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u7f51\u7edc\u8bf7\u6c42\u4e0e\u54cd\u5e94\u8bbe\u7f6e", None))
        self.request_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u65b9\u5f0f", None))
        self.combo_request_method.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"GET", None))
        self.combo_request_method.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"POST", None))
        self.combo_request_method.setItemText(2, QCoreApplication.translate("ConfigurationEditor", u"PUT", None))
        self.combo_request_method.setItemText(3, QCoreApplication.translate("ConfigurationEditor", u"DELETE", None))

        self.request_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u54cd\u5e94\u6570\u636e\u7f16\u7801", None))
        self.combo_response_encoding.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"UTF-8", None))

        self.request_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.check_verify.setText(QCoreApplication.translate("ConfigurationEditor", u"\u8bc1\u4e66\u9a8c\u8bc1", None))
        self.group_headers.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u5934", None))
        self.btn_headers_parse.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7c98\u8d34", None))
        self.btn_headers_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_headers_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_data_form.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u6570\u636e\u8868\u5355(\u76f4\u63a5\u586b\u5199)", None))
        self.btn_data_form_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_data_form_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_data_form_script.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u8bf7\u6c42\u6570\u636e\u8868\u5355(\u811a\u672c\u751f\u6210)", None))
        self.btn_data_form_script_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_data_form_script_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_cookies.setTitle(QCoreApplication.translate("ConfigurationEditor", u"Cookies", None))
        self.btn_cookies_parse.setText(QCoreApplication.translate("ConfigurationEditor", u"\u7c98\u8d34", None))
        self.btn_cookies_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_cookies_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_user_agent_pool.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u7528\u6237\u4ee3\u7406\u6c60", None))
        self.group_ip_proxy_pool.setTitle(QCoreApplication.translate("ConfigurationEditor", u"IP\u4ee3\u7406\u6c60", None))
        self.group_parse.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u89e3\u6790", None))
        self.parse_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u7c7b\u578b", None))

        self.group_data_cut.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u54cd\u5e94\u6570\u636e\u5207\u5206", None))
        self.data_cut_label1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6807\u7b7e\u540d\u79f0", None))
        self.data_cut_label2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6807\u7b7e\u5c5e\u6027", None))
        self.group_parse_setting.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u89e3\u6790\u8bbe\u7f6e", None))
        self.pset_text_label1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u7c7b\u578b: \u6587\u672c", None))
        self.btn_pset_text_add.setText(QCoreApplication.translate("ConfigurationEditor", u"\u65b0\u589e", None))
        self.btn_pset_text_delete.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5220\u9664", None))
        self.group_save.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u5b58\u50a8", None))
        self.data_save_lable1.setText(QCoreApplication.translate("ConfigurationEditor", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.combo_data_save_path.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"\u8ddf\u968f\u8bbe\u7f6e", None))
        self.combo_data_save_path.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"\u81ea\u5b9a\u4e49", None))

        self.btn_data_save_path.setText(QCoreApplication.translate("ConfigurationEditor", u"\u9009\u62e9\u4f4d\u7f6e", None))
        self.group_save_text.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u6587\u672c\u6570\u636e", None))
        self.data_save_lable2.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u7c7b\u578b", None))
        self.combo_save_text_file_type.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"TXT", None))
        self.combo_save_text_file_type.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"EXCEL", None))
        self.combo_save_text_file_type.setItemText(2, QCoreApplication.translate("ConfigurationEditor", u"SQL", None))

        self.data_save_lable3.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u540d\u79f0", None))
        self.check_save_text_paging.setText(QCoreApplication.translate("ConfigurationEditor", u"\u6570\u636e\u5206\u9875", None))
        self.data_save_lable4.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5355\u9875\u6570\u636e\u4e0a\u9650", None))
        self.group_save_image.setTitle(QCoreApplication.translate("ConfigurationEditor", u"\u4e8c\u8fdb\u5236-\u56fe\u7247", None))
        self.data_save_lable5.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u7c7b\u578b", None))
        self.combo_save_image_file_type.setItemText(0, QCoreApplication.translate("ConfigurationEditor", u"JPG", None))
        self.combo_save_image_file_type.setItemText(1, QCoreApplication.translate("ConfigurationEditor", u"PNG", None))

        self.data_save_lable6.setText(QCoreApplication.translate("ConfigurationEditor", u"\u5b58\u50a8\u6587\u4ef6\u540d\u79f0", None))

    # retranslateUi
