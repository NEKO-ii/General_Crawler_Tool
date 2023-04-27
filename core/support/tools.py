# 实用小工具
# ///////////////////////////////////////////////////////////////
from time import strftime, time, localtime


class Tools:

    def __init__(self) -> None:
        pass

    @staticmethod
    def datetime(format: str = "%Y.%m.%d %H:%M:%S") -> str:
        """返回格式化时间字符串

        Args:
            format (str, optional): 时间格式. Defaults to "%Y.%m.%d %H:%M:%S".

        Returns:
            str:
        """
        return strftime(format, localtime(time()))

    @staticmethod
    def toPagingDict(datalist: list, limit: int) -> dict:
        """数据列表转为分页数据字典

        Args:
            datalist (list): 数据列表
            limit (int): 单页数据项数量上限

        Returns:
            dict: 返回分页数据字典
        """
        datadict: dict = {}
        length = len(datalist)
        pagenum = length // limit
        startnum = 1
        if length % limit != 0:
            pagenum += 1
        for i in range(1, pagenum + 1):
            pagename = F"Page{i} {startnum}-{startnum + limit - 1 if i != pagenum else length}"
            startnum += limit
            if i == pagenum:
                datadict[pagename] = datalist[limit * (i - 1):]
            else:
                datadict[pagename] = datalist[limit * (i - 1):limit * i]
        return datadict
