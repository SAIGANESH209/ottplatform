"""
URL configuration for ottplatform project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('ottplatfromapp.urls')),
    #path('api-auth/',include('rest_framework.urls')), #it is used for temporory login
]

"""
active=Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
staff status=Designates whether the user can log into this admin site.
superuserstatus=Designates that this user has all permissions without explicitly assigning them.
    user1:admin(active,staff status,superuserstatus)
    password:admin 
    user2:ganesh(active)
    password:Amma209@
    
    """
