from django.urls import path
from . import views


urlpatterns = [
        path('', views.homePage, name='home'),
        path('about/', views.aboutPage, name='about'),
        path('add/', views.addPage, name='add'),
        path('subtract/', views.subtractPage, name='subtract'),
        path('multiply/', views.multiplyPage, name='multiply'),
        path('divide/', views.dividePage, name='divide'),

    ]
