from .Ui_AnalysisPage import Ui_AnalysisPage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from ui.dialog import Select, Notice
from ui.preload.imp_qt import QFileDialog
from core.sys.file import File, SysPath, DataType
from re import compile


class Func_AnalysisPage:
    ui: Ui_AnalysisPage
    figure = None

    flag_dataLoaded: bool = False
    colIndexLimit: int = 0

    def __init__(self, ui: Ui_AnalysisPage) -> None:
        self.ui = ui
        self.select = Select()
        self._btnConnect()
        self._sigConnect()

    def _btnConnect(self) -> None:
        self.ui.btn_run.clicked.connect(self.btn_run_clicked)
        self.ui.btn_selectTD.clicked.connect(self.btn_select_td)
        self.ui.btn_selectFile.clicked.connect(self.btn_select_file)
        self.ui.btn_clearData.clicked.connect(self.btn_clear_data)

    def _sigConnect(self) -> None:
        pass

    # 按钮响应槽函数
    # ///////////////////////////////////////////////////////////////
    def btn_run_clicked(self) -> None:
        if self.figure is not None: self.ui.vly_pic.removeWidget(self.figure)
        if self.flag_dataLoaded:
            try:
                xindex = self.ui.spin_xindex.value() - 1
                yindex = self.ui.spin_yindex.value() - 1
                isxstr = self.ui.check_x.isChecked()
                isystr = self.ui.check_y.isChecked()
                data = self.ui.table_data.c_getData(onlyCol=[xindex, yindex])
                xdata: list = []
                ydata: list = []
                if xindex < yindex:
                    for item in data:
                        xdata.append(item[0])
                        ydata.append(item[1])
                elif xindex > yindex:
                    for item in data:
                        xdata.append(item[1])
                        ydata.append(item[0])
                else:
                    xdata = [item[0] for item in data]
                    ydata = xdata
                pattern = compile(r"([+-]?[0-9]+\.?[0-9]+)")
                if isxstr:
                    xdata = [float(pattern.findall(i)[0]) for i in xdata]
                else:
                    xdata = [float(i) for i in xdata]
                if isystr:
                    ydata = [float(pattern.findall(i)[0]) for i in ydata]
                else:
                    ydata = [float(i) for i in ydata]
                self.figure = CFigure()
                self.ui.vly_pic.addWidget(self.figure)
                self.figure.axes.scatter(xdata, ydata)
            except Exception as e:
                Notice().exec("错误", F"数据分析过程发生解析错误\n检查数据源对应列是否为数字\n{e}", "error")
        else:
            Notice().exec("提示", "未加载数据源")

    def btn_select_file(self) -> None:
        # path, _ = QFileDialog.getOpenFileName(None, "选择数据文件", filter="Excel文件(*.xls *.xlsx)")
        Notice().exec("提示", "功能暂未完成")

    def btn_select_td(self) -> None:
        slist = File.read_opt(File.path(SysPath.CACHE, "temp_parse.dat"), DataType.LIST, "#")
        sshow = []
        for row in slist:
            t = eval(row)
            sshow.append([t[0], t[1], t[2], File.fileSizeConversion(int(t[6]))])
        code, selected = self.select.exec(["文件名", "数据类型", "时间", "大小"], sshow, [200, 60, 200])
        if code == 1:
            self.ui.table_data.clear()
            self.ui.ledit_filePath.clear()
            self.flag_dataLoaded = False
            path = File.path(SysPath.TEMP, "parseout", selected[0][0])
            try:
                data = eval(File.read(path))
                colcount = len(data[0])
                self.ui.table_data.c_setHeader([F"COL:{i+1}" for i in range(colcount)])
                self.ui.table_data.c_addRows(data)
                self.ui.ledit_filePath.setText(path)
                self.flag_dataLoaded = True
                self.colIndexLimit = colcount
                self.ui.spin_xindex.setMaximum(self.colIndexLimit)
                self.ui.spin_yindex.setMaximum(self.colIndexLimit)
            except Exception as e:
                Notice().exec("错误", F"数据解析失败\n{e}", "error")

    def btn_clear_data(self) -> None:
        self.flag_dataLoaded = False
        self.ui.table_data.clear()
        self.ui.ledit_filePath.clear()
        for i in range(self.ui.table_data.horizontalHeader().count()):
            self.ui.table_data.takeHorizontalHeaderItem(i)
            self.ui.table_data.setColumnCount(0)

    # 信号响应槽函数
    # ///////////////////////////////////////////////////////////////


class CFigure(FigureCanvasQTAgg):
    figure: Figure
    axes: Axes

    def __init__(self, figure=None):
        if figure is None:
            self.figure = Figure((1, 1), dpi=100)
        else:
            self.figure = figure
        super(CFigure, self).__init__(self.figure)
        self.axes = self.figure.add_subplot()
