from django.urls import path
from .views import comment_list, comment_detail

urlpatterns = [
    path('', comment_list, name='comment_list'),
    
]
