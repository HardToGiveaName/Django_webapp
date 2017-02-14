"""DjangoLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from DjangoLearning import view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', view.res_hello_view_request),
    url(r'^2017/(?P<month>\d{1,2})/(?P<day>[0-3][0-9])/$', view.res_date_view_request),
    url(r'^datetime/(\d{1,2})/$', view.res_datetime_view_request),
]
