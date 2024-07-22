"""
URL configuration for hospital project.

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
from home.views import *
from appointment.views import *
urlpatterns = [
    path('',home,name="home"),
    path('register/',register_view,name="register"),
    path('login/',login_view,name="login"),
    path('doc-login/',doc_login,name="doc-login"),  
    path('logout/',logout_view,name="logout"),
    path('appointment/', appointment_view, name="appointment"),
    path('dashboard/',dashboard_view,name="dashboard"),
    path('admin/', admin.site.urls),
    path('delete-appointment/<id>/',delete_appointment,name="delete-appointment"),
    path('update-appointment/<id>/',update_appointment,name="update-appointment"),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
