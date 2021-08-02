# -*- coding:utf-8 -*-
import json


# 判断是否为空
def isBlank(a):
    return (a is None) or (len(a) == 0)


# 获取接收参数
def getParams(request):
    if request.method == "POST":
        pass


# 返回参数的格式, 200,成功  500 失败
def returnData(content, msg, code=20000):
    return json.dumps({'content':content, 'msg': msg, 'code': code})
