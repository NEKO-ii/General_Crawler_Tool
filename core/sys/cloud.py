# 云服务模块
# ///////////////////////////////////////////////////////////////
import requests
import json


def login(username: str, password: str) -> dict:
    response = requests.post(F"http://localhost:2333/nekoverse/sys/login/{username}/{password}")
    return json.loads(response.text)


def signup(username: str, password: str, email: str) -> dict:
    response = requests.post(F"http://localhost:2333/nekoverse/sys/signup/{username}/{password}/{email}")
    return json.loads(response.text)


def getHeadImage(userid: str, himgtype: str) -> dict:
    response = requests.post(F"http://localhost:2333/nekoverse/sys/getheadimage/{userid}/{himgtype}")
    return json.loads(response.text)


def deleteAccount(userId: int) -> dict:
    response = requests.post(F"http://localhost:2333/nekoverse/sys/delaccount/{userId}")
    return json.loads(response.text)


def isUserExists(method: str, value: str) -> dict:
    response = requests.get(F"http://localhost:2333/nekoverse/sys/isuserexists/{method}/{value}")
    return json.loads(response.text)


def updatePassword(username: str, password: str) -> dict:
    response = requests.post(F"http://localhost:2333/nekoverse/sys/update/password/{username}/{password}")
    return json.loads(response.text)
