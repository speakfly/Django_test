"""hrm URL Configuration

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
    url(r'^all_upload/',app_views.all_upload),
    url(r'^logistics_upload/',app_views.logistics_upload),
    url(r'^sales_upload/',app_views.sales_upload),
    url(r'^workshop_upload/',app_views.workshop_upload),
    url(r'^money_upload/',app_views.money_upload),
    url(r'^checking_in_upload/',app_views.checking_in_upload),
    url(r'^enployee_upload/',app_views.enployee_upload),
    url(r'^profession_upload/',app_views.profession_upload),
    url(r'^department_upload/',app_views.department_upload),
    url(r'^login/',app_views.login),
    url(r'^index/',app_views.index),
    url(r'^logout/',app_views.logout),
    url(r'^updatepassword/',app_views.updatepassword),
    url(r'^department_exmaple_download/',app_views.department_exmaple_download),
    url(r'^profession_exmaple_download/',app_views.profession_exmaple_download),
    url(r'^enployee_exmaple_download/',app_views.enployee_exmaple_download),
    url(r'^train_exmaple_download/',app_views.train_exmaple_download),
    url(r'^checking_in_exmaple_download/',app_views.checking_in_exmaple_download),
    url(r'^money_exmaple_download/',app_views.money_exmaple_download),
    url(r'^workshop_exmaple_download/',app_views.workshop_exmaple_download),
    url(r'^sales_exmaple_download/',app_views.sales_exmaple_download),
    url(r'^logistics_exmaple_download/',app_views.logistics_exmaple_download),
]
