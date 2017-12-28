"""dj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views as app_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',app_views.login),
    url(r'^index/$',app_views.index),
    url(r'^logout/$',app_views.logout),
    url(r'^displayrepair/$',app_views.displayrepair),
    url(r'^repair/$',app_views.repair),
    url(r'^updatepassword/$',app_views.updatepassword),
    url(r'^displaynotice/',app_views.displaynotice),
    url(r'^academy_exmaple_download/',app_views.academy_exmaple_download),
    url(r'^academy_upload/',app_views.academy_upload),
    url(r'^major_exmaple_download/',app_views.major_exmaple_download),
    url(r'^major_upload/',app_views.major_upload),
    url(r'^grade_exmaple_download/',app_views.grade_exmaple_download),
    url(r'^grade_upload/',app_views.grade_upload),
    url(r'^apartment_exmaple_download/',app_views.apartment_exmaple_download),
    url(r'^apartment_upload/',app_views.apartment_upload),
    url(r'^room_exmaple_download/',app_views.room_exmaple_download),
    url(r'^room_upload/',app_views.room_upload),
    url(r'^student_exmaple_download/',app_views.student_exmaple_download),
    url(r'^student_upload/',app_views.student_upload),
    url(r'^all_upload/',app_views.all_upload),  
    url(r'^search_notice/',app_views.search_notice),
]
