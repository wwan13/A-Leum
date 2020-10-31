"""ALeum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('create_detail/<int:disabled_id>',views.create_detail, name='create_detail'),
    path('conconnect_detail_disable/<int:disabled_id>/<int:detail_id>',views.connect_detail_disable,name='connect_detail_disable'),
    path('create_disabled',views.create_disabled, name='create_disabled'),
]
