from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_root, name='dashboard_root'),
    path('user-list/', user_list, name='user_list'),
    path('user/<str:user_id>/', user_summary, name='user_summary'),
]