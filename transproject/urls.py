"""
URL configuration for transproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from transapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index2.html/', views.con_btn),
    path('txt_opt.html/', views.trans_btn),
    path('trans.html/', views.again_btn),
    path('txt_to_txt.html/', views.t_to_t),
    path('voice_to_voice.html/', views.v_to_v),
    path('voice_opt.html/', views.voice_recog),
]
