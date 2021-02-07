from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('', views.WidgetCreate.as_view(), name='widget_list'),
  path('', views.widget_list, name='list'),
  
  
  
]