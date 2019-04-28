
import requests

class HttpUtils:
    ## http工具
    def __init__(self):
        ## 初始化pc与wap的User_Agent
        self.User_Agent_PC = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        self.User_Agent_WAP = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"

    ## 获取pc版本的User_Agent
    def getHeadersPc(self):
        headers = {"User-Agent": self.User_Agent_PC}
        return headers

    ## 获取wap版本的User_Agent
    def getHeadersWap(self):
        headers = {"User-Agent": self.User_Agent_WAP}
        return headers
