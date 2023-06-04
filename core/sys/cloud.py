# 云服务模块
# ///////////////////////////////////////////////////////////////
import requests
import json
from core.sys.globalv import Globalv, GlvKey
from core.sys.accountstate import AccountState

# IP地址
host: str = "localhost"
# host: str = "124.238.94.67"
# host: str = "nekoverse.tpddns.cn"

# Account
# ///////////////////////////////////////////////////////////////
def updateLocalAccountState() -> None:
    accountState: AccountState = Globalv.get(GlvKey.ACCOUNT_STATE)
    accountState.update(getUserInfo(accountState._userId)["data"])


def login(username: str, password: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/login/{username}/{password}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getUserInfo(userId: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/userinfo/{userId}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def signup(username: str, password: str, email: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/signup/{username}/{password}/{email}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getHeadImage(userid: str, himgtype: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/getheadimage/{userid}/{himgtype}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def deleteAccount(userId: int) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/delaccount/{userId}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def isUserExists(method: str, value: str) -> dict:
    response = requests.get(F"http://{host}:23333/nekoverse/sys/isuserexists/{method}/{value}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def updatePassword(username: str, password: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/update/password/{username}/{password}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def uploadHeadImage(form: dict, files) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/sys/uploadheadimage", data=form, files=files)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


# Configuration
# ///////////////////////////////////////////////////////////////
def uploadConfiguration(form: dict, files: dict) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/upload", data=form, files=files)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getConfigFileList(userId: int) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/getconffs/{userId}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getConfigList(userId: int, isShared: int) -> dict:
    """获取云端配置信息

    Args:
        userId (int): 用户ID
        isShared (int): 是否共享[-1:不限, 0:未共享, 1:已共享]

    Returns:
        dict: 返回服务器响应
    """
    response = requests.post(F"http://{host}:23333/nekoverse/conf/getconfs/{userId}/{isShared}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getConfigInfo(configId: int) -> dict:
    response = requests.get(F"http://{host}:23333/nekoverse/conf/info/get/{configId}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getConfigDoc(docfname: str) -> dict:
    response = requests.get(F"http://{host}:23333/nekoverse/conf/doc/get/{docfname}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getConfigContent(userId: int, conffname: str) -> dict:
    response = requests.get(F"http://{host}:23333/nekoverse/conf/content/get/{userId}/{conffname}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def updateShareState(form: dict) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/set/sharestate", data=form)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def updateConfig(form: dict) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/update", data=form)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def deleteConfig(form: dict) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/delete", data=form)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def downloadConfig(form: dict) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/download", data=form)
    jsondata = json.loads(response.text)
    response.close()
    return jsondata


def getSharedConfig(shost: str) -> dict:
    response = requests.post(F"http://{host}:23333/nekoverse/conf/get/shared/{shost}")
    jsondata = json.loads(response.text)
    response.close()
    return jsondata
