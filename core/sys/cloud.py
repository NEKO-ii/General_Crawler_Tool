# 云服务模块
# ///////////////////////////////////////////////////////////////
import requests
import json
from core.sys.globalv import Globalv, GlvKey
from core.sys.accountstate import AccountState


# Account
# ///////////////////////////////////////////////////////////////
def updateLocalAccountState() -> None:
    accountState: AccountState = Globalv.get(GlvKey.ACCOUNT_STATE)
    accountState.update(getUserInfo(accountState._userId)["data"])


def login(username: str, password: str) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/login/{username}/{password}")
    return json.loads(response.text)


def getUserInfo(userId: str) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/userinfo/{userId}")
    return json.loads(response.text)


def signup(username: str, password: str, email: str) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/signup/{username}/{password}/{email}")
    return json.loads(response.text)


def getHeadImage(userid: str, himgtype: str) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/getheadimage/{userid}/{himgtype}")
    return json.loads(response.text)


def deleteAccount(userId: int) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/delaccount/{userId}")
    return json.loads(response.text)


def isUserExists(method: str, value: str) -> dict:
    response = requests.get(F"http://localhost:23333/nekoverse/sys/isuserexists/{method}/{value}")
    return json.loads(response.text)


def updatePassword(username: str, password: str) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/sys/update/password/{username}/{password}")
    return json.loads(response.text)


# Configuration
# ///////////////////////////////////////////////////////////////
def uploadConfiguration(form: dict, files: dict) -> dict:
    response = requests.post("http://localhost:23333/nekoverse/conf/upload", data=form, files=files)
    return json.loads(response.text)


def getConfigFileList(userId: int) -> dict:
    response = requests.post(F"http://localhost:23333/nekoverse/conf/getconffs/{userId}")
    return json.loads(response.text)


def getConfigList(userId: int, isShared: int) -> dict:
    """获取云端配置信息

    Args:
        userId (int): 用户ID
        isShared (int): 是否共享[-1:不限, 0:未共享, 1:已共享]

    Returns:
        dict: 返回服务器响应
    """
    response = requests.post(F"http://localhost:23333/nekoverse/conf/getconfs/{userId}/{isShared}")
    return json.loads(response.text)


def getConfig(configId: int) -> dict:
    response = requests.get(F"http://localhost:23333/nekoverse/conf/get/{configId}")
    return json.loads(response.text)


def updateShareState(form: dict) -> dict:
    response = requests.post("http://localhost:23333/nekoverse/conf/set/sharestate", data=form)
    return json.loads(response.text)


def deleteConfig(form: dict) -> dict:
    response = requests.post("http://localhost:23333/nekoverse/conf/delete", data=form)
    return json.loads(response.text)
