# coding = utf-8

import urllib.request
import urllib.parse


# GET

def tiebaSpider(url, beginPage, endPage):
    """
    作用： 负责处理url， 分配每个url去发送请求
    :param url: 需要处理的第一个url
    :param beginPage: 爬虫执行的起始页面
    :param endPage: 爬虫执行的截止页面
    :return:
    """
    for page in range(beginPage, endPage+1):
        pn = (page - 1) * 50
        filename = "第"+str(page)+"页.html"

        # 组合为完整的url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        print(fullurl)

        # 调用loadPage()发送请求获取html页面
        html = loadPage(fullurl, filename)

        # 将获取到的html页面写入本地磁盘文件
        writeFile(html, filename)


def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: 需要爬取的url地址
    :param filename: 文件名
    :return:
    """
    print("正在下载"+filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()


def writeFile(html, filename):
    """
    作用：保存服务器响应文件到本地磁盘文件里
    :param html: 服务器响应文件
    :param filename: 本地磁盘文件名
    :return:
    """
    print("正在存储"+filename)

    with open(filename, 'wb') as f:
        f.write(html)
    print("--"*20)

if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧：")

    # 输入起始页和终止页
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})

    url = url + key
    tiebaSpider(url, beginPage, endPage)
