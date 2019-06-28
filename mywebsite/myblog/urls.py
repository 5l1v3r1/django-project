from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="blog-home"),
    path('contact/',views.contact,name="blog-contact"),
    path('test1/',views.test1,name="blog-test1"),
    path('test2/',views.test2,name="blog-test2")
]