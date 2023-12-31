"""
URL configuration for project6_insertingby_views project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    ## Url for retrieving_topic
    path('display_topics/', display_topics, name='display_topics'),

    ## Url for retrieving_webpages
    path('display_webpages/', display_webpages, name='display_webpages'),
    
    ## Url for retrieving_access_records
    path('display_accessrecords/', display_accessrecords, name='display_accessrecords'),

    path('display_all/', display_all, name='display_all'),


    path('update_webpage/', update_webpage, name='update_webpage'),

]