# coding = utf-8
# 编码工作使用urllib.parse 的 urlencode()函数，帮我们将key:value 这样的键值对转换成 key=value这样的字符串
# 解码工作使用urllib.parse 的 unquote() 函数
import urllib.request
import urllib.parse

word = {'wd': '创造'}

# 通过urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受
str = urllib.parse.urlencode(word)
print(str)

# 通过unquote() 方法，把url编码字符串，转换回原先字符串
dicStr = urllib.parse.unquote(str)
print(dicStr)


# Get请求
def get_Test():
    url = "http://www.baidu.com/s"
    word = {"wd": "传智播客"}

    word = urllib.parse.urlencode(word)
    newurl = url + '?' + word
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    request = urllib.request.Request(newurl, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.code)
    print(response.read())

get_Test()