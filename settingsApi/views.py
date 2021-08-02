from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET

from utils.common import *
from .models import *
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


"""配置文件"""


# 新增or修改配置文件
@require_POST
def mergeSetting(request):
    # 检查数据
    result = checkSettingField(request.GET)
    if len(result) > 0:
        return HttpResponse(returnData("", result))

    # 获取配置文件的id，若位空则为新增，反之为修改
    setting_id = request.GET.get("id")
    if isBlank(setting_id):
        new_s = settings(name=request.GET.get("name"), desc=request.GET.get("desc"))
        new_s.save()
    else:
        # 修改配置文件
        setting = settings.objects.get(id=setting_id)
        setting.name = request.GET.get("name")
        setting.desc = request.GET.get("desc")
        setting.save()
    result = returnData("", "操作成功")
    return HttpResponse(result)


# 获取文件名称
@require_GET
def getSettings(request):
    all_setting = [i.getJson() for i in settings.objects.all()]
    return HttpResponse(returnData(all_setting, "请求成功"))


# 检测数据格式
def checkSettingField(params):
    result = ''
    if params.get("name") is None or params.get("name") == "":
        result = result + '配置文件名称不能为空\n'
    old_s = settings.objects.filter(name=params.get("name"))
    if len(old_s) > 0:
        result = result + '已存在该名称的配置文件\n'
    return result


""" 配置文件详情 """


# 新增or更新配置详情
@require_POST
def mergeSettingDetail(request):
    # 检查数据完整性
    result = checkSettingDetailField(request.GET)
    if len(result) > 0:
        return returnData("", result)

    # 配置详情id为空，则为新增，不为空为修改
    if request.GET.get("id") is None:
        foreignKey = settings.objects.get(id=request.GET.get("sid"))
        s_detail = setting_details(pid=0 if request.GET.get("pid") is None or request.GET.get("pid") == '' else request.GET.get("pid"),
                                   name=request.GET.get("name"),
                                   value=request.GET.get("value"),
                                   desc=request.GET.get("desc"),
                                   sid=foreignKey)
    else:
        s_detail = setting_details.objects.get(id=request.GET.get("id"))
        s_detail.desc = request.GET.get("desc")
        s_detail.name = request.GET.get("name")
        s_detail.value = request.GET.get("value")
        s_detail.sid = request.GET.get("sid")
    s_detail.save()
    result = returnData("", "操作成功")
    return HttpResponse(result)


def checkSettingDetailField(params):
    result = ''
    if params.get("sid") is None or params.get("sid") == "":
        result += '所属配置文件ID为空\n'
    if params.get("name") is None or params.get("name") == "":
        result += '配置项名称为空\n'
    # if params.get("value") is None or params.get("value") == "":
    #     result += '配置项值为空\n'
    return result


# 获取配置详情
@require_GET
def getSettingDetail(request):
    sds = setting_details.objects.filter(sid=request.GET.get("sid"), pid=request.GET.get("pid"))
    result = returnData([sd.getJson() for sd in sds], "请求成功")
    return HttpResponse(result)


@require_POST
def delSettingDetail(request):
    data = json.loads(request.body)
    ids = data.get("ids")
    sds = setting_details.objects.filter(id__in=ids)
    for i in sds:
        i.delete()
    result = returnData("", "请求成功")
    return HttpResponse(result)
