# JS代码执行器
# ///////////////////////////////////////////////////////////////
import execjs
import subprocess
from core.sys.file import File
import json


def runjs(scriptPath: str, args) -> tuple[bool, dict, str]:
    """执行JS脚本

    Args:
        scriptPath (str): 脚本绝对路径
        args (list): 参数列表

    Returns:
        tuple[bool, dict, str]: 返回元组,包括执行结果,脚本返回的数据字典,错误信息
    """
    code = File.read(scriptPath)
    result = None
    try:
        comp = execjs.compile(code)
        if args:
            result = comp.call("run", args)
        else:
            result = comp.call("run")
    except Exception as e:
        return (False, None, e.__repr__())
    try:
        if result:
            # result = json.dumps(eval(str(result)))
            result = str(result)
            return (True, json.loads(result), "数据解析成功")
        else:
            return (True, None, "脚本成功运行但未输出任何数据")
    except Exception as e:
        return (False, str(result), e.__repr__())


def runpy(scriptPath: str, args) -> tuple[bool, dict, str]:
    """执行Python脚本

    Args:
        scriptPath (str): 脚本绝对路径
        args (list): 参数列表

    Returns:
        tuple[bool, dict, str]: 返回元组,包括执行结果,脚本返回的数据字典,错误信息
    """
    cmd = ["python", "-Xfrozen_modules=off", scriptPath]
    for item in args:
        cmd.append(item)
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as popen:
        result = None
        err = None
        result, err = popen.communicate()
        # if popen.stdout:
        #     result = str(popen.stdout.read().decode())
        # if popen.stderr:
        #     err = str(popen.stderr.read())
    if err:
        err = err.decode()
        return (False, None, err)
    else:
        try:
            if result:
                result = json.dumps(eval(result.decode()))
                return (True, json.loads(result), "数据解析成功")
            else:
                return (True, None, "脚本成功运行但未输出任何数据")
        except Exception as e:
            return (False, result, e.__repr__())
