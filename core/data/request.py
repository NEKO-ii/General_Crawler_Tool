from requests import get, post, put, delete, head, options, Response, Session
from requests.cookies import RequestsCookieJar

func: dict = {"get": get, "post": post, "put": put, "delete": delete, "head": head, "options": options}


class Request(object):
    """网络请求类"""

    def __init__(self) -> None:
        pass

    # TODO: Auth身份验证
    # TODO: session会话维持的深入设置
    @staticmethod
    def run(method: str, url: str, headers: dict = {}, data_form: dict = {}, cookies: dict = {}, verify: bool = True, timeout: float = 10.0) -> Response:
        headers["Host"] = url.split("//")[-1].split("/", 1)[0]
        cookie_jar = RequestsCookieJar()
        for key, value in cookies.items():
            cookie_jar.set(key, value)
        # session = Session()
        return func[method](url, headers=headers, data=data_form, cookies=cookies, verify=verify, timeout=timeout)
