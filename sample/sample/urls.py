from django.contrib import admin
from django.urls import path, include
from sampleapp import views

urlpatterns = [
    path('', views.hello_world),      # Home page
    path('admin/', admin.site.urls),
    path('app/', include('sampleapp.urls')),
]