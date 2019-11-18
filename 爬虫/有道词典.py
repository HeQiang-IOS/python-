# coding=utf-8

import urllib.request
import urllib.parse

# 1、导入python SSL 处理模块
import ssl

# 2、表示忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

def test1():
    # POST请求的目标URL
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {"User-Agent": "Mozilla...."}

    formdata = {
        "type": "AUTO",
        "i": "i love python",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    data = urllib.parse.urlencode(formdata).encode("utf-8")
    request = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(request, context=context)
    print(response.read().decode("utf-8"))


def test2():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

    headers = {"User-Agent": "Mozilla...."}

    # 变动的是这两个参数，从start开始往后显示limit个
    formdata = {
        'start': '0',
        'limit': '10'
    }

    data = urllib.parse.urlencode(formdata).encode("utf-8")
    request = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(request, context=context)
    print(response.read().decode('utf-8'))

def test3():
    url = "https://movie.douban.com/j/chart/top_list?"
    headers = {"User-Agent": "Mozilla...."}

    # 处理所有参数
    formdata = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '10'
    }
    data = urllib.parse.urlencode(formdata).encode("utf-8")

    request = urllib.request.Request(url, data=data, headers=headers)

    response = urllib.request.urlopen(request, context=context)

    print(response.read().decode('utf-8'))

if __name__ == "__main__":
    test2()