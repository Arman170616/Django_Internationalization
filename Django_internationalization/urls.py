
from django.contrib import admin
from django.urls import path
from example import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
