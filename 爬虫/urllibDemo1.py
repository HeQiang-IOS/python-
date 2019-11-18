# coding = utf-8

# urllib模块的基本使用

import urllib.request
import random

def test1():
    # 向指定的url发送请求，并返回服务器响应的类文件对象
    response = urllib.request.urlopen("http://www.baidu.com")

    # 类文件对象支持 文件对象的操作方法， 如read()方法读取文件全部内容，返回字符串
    html = response.read()
    # 打印字符串
    print(html)

def test2():
    # url 作为Request()方法的参数，构造并返回一个Request对象
    request = urllib.request.Request('http://www.baidu.com')

    # Requset对象作为urlopen()方法的参数，发送给服务器并接收响应
    response = urllib.request.urlopen(request)

    html = response.read()

    print(html)

def test3():
    url = 'http://www.itcast.cn'
    # IE 9.0 的 User-Agent，包含在 ua_header里
    ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    # url 连同 headers, 一起构造Request请求，这个请求将附带 IE9.0 浏览器的User-Agent
    request = urllib.request.Request(url, headers=ua_header)

    # 也可以通过调用Request.add_header()方法，添加/修改一个特定的header
    request.add_header("Connection", "keep-alive")

    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
    ]

    user_agent = random.choice(ua_list)

    request.add_header("User-Agent", user_agent)

    # 第一个字母大写，后面的全部小写
    request.get_header('User-agent')


    # 向服务器发送这个请求
    response = urllib.request.urlopen(request)

    print(response.code)

    html = response.read()

    print(html)

test3()