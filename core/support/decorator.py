# 函数/方法修饰器模块,所有修饰器在此处定义
# ///////////////////////////////////////////////////////////////
from core.support.msg_printer import MsgType, console_printer
from core.support.initialize import init_settings


class Decorator:
    """修饰器类
    """

    @staticmethod
    def settings_load(func):
        """设置文件读取时触发,若读取出错(文件损坏)则将设置文件恢复默认并重新读取
        """

        def ncp_inner(*args, **kwargs):
            retn = None
            try:
                retn = func(*args, **kwargs)
            except Exception as e:
                console_printer(MsgType.WARNING, "Settings file damaged, the settings have been restored to default")
                init_settings()
                retn = func(*args, **kwargs)
                return retn
            return retn

        return ncp_inner

    @staticmethod
    def config_load(func):
        """读取配置文件时触发,拦截严重错误(如无法解析JSON)
        """

        def ncp_inner(*args, **kwargs):
            retn = None
            try:
                retn = func(*args, **kwargs)
            except Exception as e:
                console_printer(MsgType.ERROR, F"Configuration file damaged.{e}")
            return retn

        return ncp_inner
