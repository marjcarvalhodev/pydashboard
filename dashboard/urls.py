from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list, name='user_list'),
    path('user/<str:user_id>/', user_summary, name='user_summary'),
    # add other app routes here too
]
