from utils.HttpUtils import HttpUtils
from utils.FileUtils import FileUtils
from lxml import etree
import requests


## 获取糗事百科的数据
class GetQiuShiBaiKe:
    def __init__(self):
        httpUtils = HttpUtils()
        self.url_temp = "https://www.qiushibaike.com/textnew/page/{}"
        self.headers = httpUtils.getHeadersPc()

    def run(self):
        ## 1.构建所有url
        urlList = self.getAllUrl()
        ## 2.获取页面数据
        fileUtils = FileUtils()
        for url in urlList:
            htmlContent = self.getHtmlInfo(url)
            content = self.parseHtmlContent(htmlContent)
            ## 3.保存文件
            fileUtils.saveFile("qiushibaike.txt", content, "a")

    def getAllUrl(self):
        urlList = [self.url_temp.format(i) for i in range(1, 36)]
        return urlList

    def getHtmlInfo(self, url):
        content = requests.get(url, headers=self.headers)
        return content.content.decode()

    def parseHtmlContent(self, htmlContent):
        contents = []

        htmlElement = etree.HTML(htmlContent)
        articles = htmlElement.xpath("//div[@id='content-left']/div")
        for article in articles:
            contentInfo = {}
            contentInfo['content'] = article.xpath(".//span/text()")
            contentInfo['content'] = [info.strip() for info in contentInfo['content']] if len(
                contentInfo['content']) > 0 else None;
            contentInfo['author'] = article.xpath("./div//h2/text()")[0] if len(
                article.xpath("./div//h2/text()")) > 0 else None
            contentInfo['author_img'] = "https:" + article.xpath("./div//img/@src")[0] if len(
                article.xpath("./div//img/@src")) > 0 else None
            contents.append(contentInfo)
        return contents


if __name__ == '__main__':
    getQiuShiBaiKe = GetQiuShiBaiKe()
    getQiuShiBaiKe.run()
