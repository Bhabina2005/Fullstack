from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('class/', views.HelloWorld.as_view()),
    path('reservation/', views.home),
]
