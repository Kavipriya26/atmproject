"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerviewset.as_view({'get':'list','post':'create'})),
    path('register/<int:pk>/',views.registerviewset.as_view({'delete':'destroy'})),

    path('authentication/', views.authenticationviewset.as_view({'get':'list','post':'create'})),
    path('authentication/<int:pk>/',views.authenticationviewset.as_view({'delete':'destroy'})),
   
    path('deposit/', views.depositviewset.as_view({'get':'list','post':'create'})),
    path('deposit/<int:pk>/',views.depositviewset.as_view({'delete':'destroy'})),

   path('withdraw/', views.withdrawviewset.as_view({'get':'list','post':'create'})),
   path('withdraw/<int:pk>/',views.ithdrawviewset.as_view({'delete':'destroy'})),

   path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))




]
