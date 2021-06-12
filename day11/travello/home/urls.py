from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name = 'contact'),
    path('news/',views.about, name='news'),
    
]
