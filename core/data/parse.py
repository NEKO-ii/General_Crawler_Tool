# 数据解析模块, 处理来自网络响应的信息
from re import compile, RegexFlag
from time import time
from traceback import print_exc

from bs4 import BeautifulSoup
from lxml import etree


class Parse(object):
    """数据解析类"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def pretreatment(html: str | list, tag_name: str, attrs: dict = {}) -> list:
        """响应内容预处理方法"""
        return_list: list = []
        data: list = []
        if type(html) == str: data.append(html)
        elif type(html) == list: data = html
        try:
            for item in data:
                soop = BeautifulSoup(item, "lxml")
                finds = soop.find_all(tag_name, attrs=attrs)
                for find in finds:
                    return_list.append(find)
            return return_list
        except:
            print_exc()

    @staticmethod
    def bs4_select(data: str | list, command: str, index: int | list, sep: str = " ") -> list:
        """普通文本搜索方法 bs4@select"""
        return_list: list = []
        if type(data) == str: data = [data]
        if type(index) == int: index = [index]

        for item in data:
            try:
                finds = None
                item = str(item)
                soop = BeautifulSoup(item, "lxml")
                selector, attribute = command.split("@", 1)
                finds = soop.select(selector)
                if finds:
                    if index:
                        cell = ""
                        length = finds.__len__()
                        for i in range(0, length):
                            if (i + 1) in index:
                                find = finds[i]
                                if attribute == "text":
                                    cell = sep.join([cell, find.text])
                                else:
                                    cell = sep.join([cell, find[attribute]])
                                return_list.append(cell.split(sep, 1)[1].strip())
                    else:
                        cell = ""
                        for find in finds:
                            if attribute == "text":
                                cell = sep.join([cell, find.text])
                            else:
                                cell = sep.join([cell, find[attribute]])
                        return_list.append(cell.split(sep, 1)[1].strip())
                else:
                    return_list.append("None")
            except Exception as e:
                if finds: return_list.append("None")
                print_exc()
        return return_list

    @staticmethod
    def re_findall(data: str | list, selector: str, index: int, sep: str = " ") -> list:
        """普通文本搜索方法 re@findall"""
        return_list: list = []
        flags: dict = {"S": RegexFlag.S, "A": RegexFlag.A, "I": RegexFlag.I, "M": RegexFlag.M, "L": RegexFlag.L, "T": RegexFlag.T, "U": RegexFlag.U, "X": RegexFlag.X, "0": 0}

        for item in data:
            try:
                finds = None
                item = str(item)
                comp = compile(selector, flags=0)
                finds = comp.findall(item)
                if finds:
                    if index:
                        cell = ""
                        length = finds.__len__()
                        for i in range(0, length):
                            if (i + 1) in index:
                                cell = sep.join([cell, finds[i]])
                                return_list.append(cell.split(sep, 1)[1].strip())
                    else:
                        cell = ""
                        for find in finds:
                            cell = sep.join([cell, find])
                        return_list.append(cell.split(sep, 1)[1].strip())
                else:
                    return_list.append("None")
            except Exception as e:
                if finds: return_list.append("None")
                print_exc()
        return return_list

    @staticmethod
    def lxml_xpath(data: list, selector: str, index: int, sep: str = " ") -> str:
        """普通文本搜索方法 lxml@etree@xpath"""
        return_list: list = []

        for item in data:
            try:
                finds = None
                item = str(item)
                element = etree.HTML(item)
                if selector.find("/text()") == -1 and selector.find("/@") == -1:
                    selector = "/".join([selector, "text()"])
                finds = element.xpath(selector)
                if finds:
                    if index:
                        cell = ""
                        length = finds.__len__()
                        for i in range(0, length):
                            if (i + 1) in index:
                                cell = sep.join([cell, finds[i]])
                                return_list.append(cell.split(sep, 1)[1].strip())
                    else:
                        cell = ""
                        for find in finds:
                            cell = sep.join([cell, find])
                        return_list.append(cell.split(sep, 1)[1].strip())
                else:
                    return_list.append("None")
            except Exception as e:
                if finds: return_list.append("None")
        return return_list
