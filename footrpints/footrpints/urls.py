"""
URL configuration for footrpints project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core import views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/verifyUser/', views.alumni_list),
    path('api/emailv/',v.email_verification),
    path('api/otpv/<str:email>/',v.verify_otp),
    path('api/resend/', v.resend_otp)
]
