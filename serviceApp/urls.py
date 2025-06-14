from django.urls import path
from . import views

app_name = 'serviceApp'

urlpatterns = [
    path('download/', views.download, name='download'),  # 资料下载
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'), # 下载文件
    path('facedetect/', views.facedetect, name='facedetect'),  # 人脸检测api
    path('facedetectDemo/', views.facedetectDemo, name='facedetectDemo'),  # 在线人脸检测
]



