from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    ]
