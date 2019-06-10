"""TTL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
#from TTL.apps.accounts import views
#from TTL.apps.web import views
#import TTL.apps.accounts.views




urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^$', TTL.apps.accounts.views.home, name='TTL_Home'),
    re_path(r'^app_accounts/', include('app_accounts.urls')),

    re_path(r'^app_core0/', include('app_core0.urls')),

    #re_path(r'^web/', include('app_web.urls')),

    #re_path(r'', include('TTL.apps.web.urls')),
    
]