"""assistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import views


app_name = 'newapp'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='Home'),
    url(r'^saysomething', views.saysomething, name='saysomething'),
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^notes', views.notes, name='notes'),
    url(r'^exam', views.exam, name='exam'),
    url(r'^teacher_submit/', views.teacher_submit),
    url(r'^ans_submit/', views.ans_submit),

    url(r'^question_submit/',views.question_submit),
    url(r'Submit', views.exam_submit,name='exam_submit'),

]
