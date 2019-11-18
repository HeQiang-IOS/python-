# coding=utf-8

from bs4 import  BeautifulSoup
import urllib.request
import json
import ssl

context = ssl._create_unverified_context()

def tencent():
    url = 'http://hr.tencent.com/'
    request = urllib.request.Request(url + 'position.php?&start=10#a')
    response = urllib.request.urlopen(request, context=context)
    resHtml = response.read()

    output = open("tencent.json", "bw")

    html = BeautifulSoup(resHtml, 'lxml')
    result = html.select('tr[class="even"]')
    result2 = html.select('tr[class="odd"]')
    result += result2

    items = []
    for site in result:
        item = {}

        name = site.select('td a')[0].get_text()
        detailLink = site.select('td a')[0].attrs['href']
        catalog = site.select('td')[1].get_text()
        recruitNumber = site.select('td')[2].get_text()
        workLocation = site.select('td')[3].get_text()
        publishTime = site.select('td')[4].get_text()

        item['name'] = name
        item['detailLink'] = url + detailLink
        item['catalog'] = catalog
        item['recruitNumber'] = recruitNumber
        item['publishTime'] = publishTime

        items.append(item)

    # 禁用ascii编码，按utf-8编码
    line = json.dumps(items, ensure_ascii=False)
    print(line)
    output.write(line.encode('utf-8'))
    output.close()

if __name__ == "__main__":
    tencent()