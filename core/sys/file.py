# 文件支持
# ///////////////////////////////////////////////////////////////
from enum import Enum
from json import dumps, loads
from os.path import join, normpath, isfile, exists, abspath, basename
from os import remove, removedirs, getcwd
from pandas import DataFrame, ExcelWriter

from core.support import remove_json_comments
from core.sys.globalv import Globalv, GlvKey


class DataType(Enum):
    STRING: int = 1
    LIST: int = 2
    DICTIONARY: int = 3


class SysPath(Enum):
    BASE: int = 0
    CONFIGURATION: int = 1
    SCRIPT: int = 2
    THEMES: int = 3
    SETTINGS: int = 4
    TEMP: int = 5
    LOG: int = 6
    HELP: int = 7
    INPUT: int = 8
    OUTPUT: int = 9
    CACHE: int = 10


class File:

    def __init__(self) -> None:
        pass

    @staticmethod
    def path(sys_path: SysPath = SysPath.BASE, *paths: str) -> str:
        """输入文件相对路径,返回绝对路径+相对路径,支持拆分输入

        Args:
            paths (list|str): 相对路径

        Returns:
            str: 返回组装好的绝对路径
        """
        path = Globalv.get(GlvKey.PATH)
        if sys_path == SysPath.BASE:
            return normpath(join(abspath(getcwd()), *paths))
        if sys_path == SysPath.CONFIGURATION:
            return normpath(join(path.p_configuration, *paths))
        if sys_path == SysPath.SCRIPT:
            return normpath(join(path.p_script, *paths))
        if sys_path == SysPath.THEMES:
            return normpath(join(path.p_themes, *paths))
        if sys_path == SysPath.SETTINGS:
            return normpath(join(path.p_settings, *paths))
        if sys_path == SysPath.TEMP:
            return normpath(join(path.p_temp, *paths))
        if sys_path == SysPath.LOG:
            return normpath(join(path.p_log, *paths))
        if sys_path == SysPath.HELP:
            return normpath(join(path.p_help, *paths))
        if sys_path == SysPath.INPUT:
            return normpath(join(path.p_input, *paths))
        if sys_path == SysPath.OUTPUT:
            return normpath(join(path.p_output, *paths))
        if sys_path == SysPath.CACHE:
            return normpath(join(path.p_cache, *paths))

    @staticmethod
    def pathJoin(*paths: str) -> str:
        """将输入路径连接为路径字符串"""
        return normpath(join(*paths))

    @staticmethod
    def read(path: str) -> str:
        """读取文件,返回未经处理的字符串

        Args:
            path (str): 文件地址

        Returns:
            str: 返回读取字符串
        """
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()

    @staticmethod
    def read_opt(path: str, return_type: DataType, comment_mark: str = None):
        """读取文件,依照设定进行处理后返回

        Tips:
            ReturnMode.STRING: 返回文件内容去除空行与注释行后的完整字符串
            ReturnMode.LIST: 返回文件内容去除空行与注释行后由每行内容组成的列表(不包含行尾换行符)
            ReturnMode.DICTIONARY: 返回JSON格式文件解析后的Python字典

        Args:
            path (str): 文件地址
            return_mode (ReturnMode): 返回类型
            comment_mark (str, optional): 注释标识,以该标识开头的行将被舍弃. Defaults to None.

        Returns:
            dict | str | list: 返回数据
        """
        with open(path, "r", encoding="UTF-8") as file:
            if return_type == DataType.DICTIONARY:
                return loads(remove_json_comments(file.read()))
            return_list: list = []
            line: str
            for line in file.readlines():
                if line.startswith(comment_mark) or line == "\n": continue
                else:
                    if return_type == DataType.LIST: return_list.append(line.strip())
                    else: return_list.append(line)
            if return_type == DataType.LIST:
                return return_list
            if return_type == DataType.STRING:
                return str.join([s for s in return_list])

    @staticmethod
    def write(path: str, data, mode="w") -> None:
        """将数据写入文件,自动判断输入数据类型

        Tips:
            str: 字符串类型数据将被直接写入
            list: 列表每一项为一行写入文件
            dict: 字典类型数据将转化为json字符串存入文件

        Args:
            path (str): 文件路径
            data (_type_): 数据
        """
        with open(path, mode, encoding="UTF-8") as file:
            if type(data) == str:
                file.write(data)
            elif type(data) == list:
                write_list = []
                for item in data:
                    write_list.append(str(item) + "\n")
                file.writelines(write_list)
            elif type(data) == dict:
                file.write(dumps(data, indent=2) + "\n")

    @staticmethod
    def writeWithComment(path: str, data, top_comment: str = "", bottom_comment: str = "") -> None:
        """将数据以及注释写入文件(此方法会先清空文件原有内容)

        Args:
            path (str): 文件地址
            data (_type_): 数据
            top_comment (str): 顶部注释,默认为空字符串
            bottom_comment (str): 底部注释,默认为空字符串
        """
        with open(path, "w", encoding="UTF-8") as file:
            file.write(top_comment)
            if type(data) == str:
                file.write(data)
            elif type(data) == list:
                write_list = []
                for item in data:
                    write_list.append(str(item) + "\n")
                file.writelines(write_list)
            elif type(data) == dict:
                file.write(dumps(data, indent=2) + "\n")
            file.write(bottom_comment)

    @staticmethod
    def isFileExists(path) -> bool:
        """判断文件是否存在"""
        if exists(path) and isfile(path):
            return True
        else:
            return False

    @staticmethod
    def isFolderExists(path) -> bool:
        """判断文件夹是否存在"""
        if exists(path) and not isfile(path):
            return True
        else:
            return False

    @staticmethod
    def checkFileName(fileName: str) -> bool:
        """判断输入路径是否合法"""
        for char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
            if fileName.find(char) != -1:
                return False
            else:
                return True

    @staticmethod
    def isExists(path) -> bool:
        """判断是否存在"""
        return exists(path)

    @staticmethod
    def delete(path):
        """删除路径,文件和文件夹均可"""
        if isfile(path): remove(path)
        elif exists(path): removedirs(path)

    @staticmethod
    def getBasenameFromUrl(path) -> str:
        """返回路径中的文件名"""
        return basename(path)

    @staticmethod
    def insertFileName(fileName: str, index: int, subStr: str) -> str:
        """在文件名指定位置后插入字符串

        Args:
            fileName (str): 文件名(有无后缀均可)
            index (int): 位置索引(忽略扩展名,0为起始位置,-1为末尾)
            subStr (str): 插入的字符串

        Returns:
            str: 返回修改后的文件名
        """
        if "." in fileName:
            arr = fileName.rsplit(".", 1)
            base = arr[0]
            extend = arr[1]
            if index == -1: index = base.__len__()
            return F"{base[:index]}{subStr}{base[index:]}.{extend}".strip()
        else:
            if index == -1: index = fileName.__len__()
            return F"{fileName[:index]}{subStr}{fileName[index:]}".strip()

    @staticmethod
    def createExcelFile(path: str, datadict: dict):
        """依据数据字典创建 Excel 文件

        Args:
            path (str): 文件地址
            datadict (dict): 数据字典, 字典键为 sheet 工作表名, 值为表内容
        """
        try:
            # TODO: info表数据填充
            DataFrame().to_excel(path, sheet_name="info", engine="openpyxl")
            for pagename in datadict:
                dataframe = DataFrame(datadict[pagename])
                writer = ExcelWriter(path, mode="a", engine="openpyxl")
                dataframe.to_excel(writer, sheet_name=pagename, index=False)
                # writer.save()
                writer.close()
        except Exception as e:
            #TODO 错误日志记录
            print(e)
