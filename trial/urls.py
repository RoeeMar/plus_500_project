"""trial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from plus500 import views as plus500_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view(), name="login"),
    path('home/',plus500_views.home, name="home"),
    path('export_to_csv',plus500_views.export_to_csv, name="export-csv"),
    #path('contact_send_email',plus500_views.contact_send_email),
    path('settings/',plus500_views.settings, name="settings"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include ('plus500.urls'))
]
