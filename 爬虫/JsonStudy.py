# coding=utf-8
import json
import chardet


strList = '[1, 2, 3, 4]'

strDict = '{"city": "北京", "name": "大猫"}'

print(json.loads(strList))
# Json格式字符串解码转换成Python对象

print(json.loads(strDict))


listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr = {"city": "北京", "name": "大猫"}

print(json.dumps(listStr))
# '[1, 2, 3, 4]'
json.dumps(tupleStr)
# '[1, 2, 3, 4]'
print(json.dumps(dictStr))

# chardet.detect(json.dumps(dictStr))
print(json.dumps(dictStr, ensure_ascii=False))

listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr, open("listStr.json", "w"), ensure_ascii=False)

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json", "w"), ensure_ascii=False)

strList = json.load(open("listStr.json"))
print(strList)