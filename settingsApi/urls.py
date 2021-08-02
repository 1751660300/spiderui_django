# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mergeSetting', views.mergeSetting, name='mergeSetting'),
    path('getSettings', views.getSettings, name='getSettings'),
    path('mergeSettingDetail', views.mergeSettingDetail, name='mergeSettingDetail'),
    path('getSettingDetail', views.getSettingDetail, name='getSettingDetail'),
    path('delSettingDetail', views.delSettingDetail, name='delSettingDetail'),
]