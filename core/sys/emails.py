# 邮件服务模块
# ///////////////////////////////////////////////////////////////
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from random import randint

# Outlook STMP 服务端口信息
# 服务器名称: smtp.office365.com
# 端口: 587
# 加密方法: STARTTLS


class Emails:
    _server: str = "smtp.office365.com"
    _port: int = 587
    _username: str = "lntu.NEKO@outlook.com"
    _password: str = "lemacjtzikswqody"

    smtp: smtplib.SMTP
    errmsg: str = None

    flag_connect: bool = False

    def __init__(self) -> None:
        # self.connect()
        pass

    def connect(self) -> None:
        try:
            self.smtp = smtplib.SMTP_SSL(self._server, timeout=10.0)
            self.smtp.connect(host=self._server, port=self._port)
            self.smtp.ehlo()
            # self.smtp.starttls()
            self.smtp.login(self._username, self._password)
            self.flag_connect = True
        except Exception as e:
            self.errmsg = e.__repr__()

    def close(self) -> None:
        self.smtp.close()

    def sendVerificationCode(self, targetAddr: str) -> tuple[bool, str, str]:
        """发送验证

        Args:
            targetAddr (str): 目标邮件地址

        Returns:
            tuple[bool, str, str]: 返回数据[成功与否, 验证码, 消息]
        """
        code: str = ""

        for i in range(6):
            code = code + str(randint(0, 9))
        # vmsg: str = '自动化爬虫工具(General Crawler Tool)验证邮件\n\n'
        # F'您的验证码为{code}\n\n'
        # '该验证码用于本工具的注册及修改密码操作, 请勿将该验证码发送给其他人\n'
        # '若您不知道为何收到该邮件, 请将邮件忽略\n'

        # message = MIMEText(vmsg, "plain", "utf-8")
        # message.add_header("Subject", "General Crawler Tool 验证码邮件")
        # message.add_header("From", "General Crawler Tool")
        # message.add_header("To", targetAddr)

        try:
            # self.smtp.sendmail(from_addr=self._username, to_addrs=targetAddr, msg=message.as_string())
            return (True, code, "发送成功")
        except Exception as e:
            return (False, code, e.__repr__())
