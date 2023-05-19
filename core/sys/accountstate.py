# 账户状态类
# ///////////////////////////////////////////////////////////////


class AccountState:
    _userId: int = None
    _isLoginSucceed: bool = False
    _username: str = None
    _password: str = None
    _email: str = None
    _createTime: str = None
    _updateTime: str = None
    _lastLoginTime: str = None
    _requestCount: int = None
    _configSaveCount: int = None
    _headImageType: str = None

    def __init__(self) -> None:
        pass

    def update(self, data: dict) -> None:
        self._userId = data["userId"]
        self._username = data["username"]
        self._password = data["password"]
        self._email = data["email"]
        self._createTime = data["createTime"]
        self._updateTime = data["updateTime"]
        self._lastLoginTime = data["lastLoginTime"]
        self._requestCount = data["requestCount"]
        self._configSaveCount = data["configSaveCount"]
        self._headImageType = data["headImageType"]

    def clear(self) -> None:
        self._userId: int = None
        self._isLoginSucceed: bool = False
        self._username: str = None
        self._password: str = None
        self._email: str = None
        self._createTime: str = None
        self._updateTime: str = None
        self._lastLoginTime: str = None
        self._requestCount: int = None
        self._configSaveCount: int = None
        self._headImageType: str = None
