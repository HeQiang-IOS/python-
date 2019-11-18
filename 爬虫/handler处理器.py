# coding=utf-8

# 自定义opener

import urllib.request
import random

def test1():
    # 构建一个httphandler  处理器对象， 支持处理http请求
    http_handler = urllib.request.HTTPHandler(debuglevel=1)

    # 调用 build_opener()方法，创建支持处理http请求的opener对象
    opener = urllib.request.build_opener(http_handler)

    # 构建 Request请求
    request = urllib.request.Request("http://www.baidu.com")

    # 调用自定义opener对象open()方法，发送request请求
    response = opener.open(request)

    # 获取服务器响应内容
    print(response.read())


def test2():
    """
    使用代码IP， 这是爬虫、反爬虫的第二大招，通常也是最好用的
    很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。
    所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。
    :return:
    """
    proxy_list = [
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"}
    ]

    proxy = random.choice(proxy_list)

    """
    HTTPPasswordMgrWithDefaultRealm()类将创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码，主要应用两个场景：

验证代理授权的用户名和密码 (ProxyBasicAuthHandler())
验证Web客户端的的用户名和密码 (HTTPBasicAuthHandler())

    """

    # 私密代理授权的账户
    user = "mr_mao"
    # 私密代理授权的密码
    passwd = "sff"

    # 1、构建一个密码管理对象，用来保存需要处理的用户名和密码
    passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # 2、添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
    passwdmgr.add_password(None, proxy,  user, passwd)

    # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
    #   注意，这里不再使用普通ProxyHandler类了
    proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdmgr)


    # 4、通过build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
    opener1 = urllib.request.build_opener(proxyauth_handler)

    # 构建了两个代理handler， 一个有代理IP， 一个没有代理IP
    httpproxy_handler = urllib.request.ProxyHandler(proxy)
    nullproxy_handler = urllib.request.ProxyHandler()

    proxySwitch = False

    if proxySwitch:
        opener = urllib.request.build_opener(httpproxy_handler)
    else:
        opener = urllib.request.build_opener(nullproxy_handler)

    request = urllib.request.Request("http://www.baidu.com")

    response = opener1.open(request)
    print(response.read)

    # 5. 可以选择通过install_opener()方法定义opener为全局opener
    urllib.request.install_opener(opener1)

    # 6. 构建 Request对象
    request = urllib.request.Request("http://www.baidu.com")

    # 7. 定义opener为全局opener后，可直接使用urlopen()发送请求
    response = urllib.request.urlopen(request)
    print(response.read)

if __name__ == "__main__":
    test2()