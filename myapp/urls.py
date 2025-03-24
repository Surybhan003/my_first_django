from django.urls import path
from .views import contact_view, success_view, home

urlpatterns = [
    path("",home, name="home"),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
