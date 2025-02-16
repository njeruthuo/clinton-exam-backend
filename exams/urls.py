from django.urls import path
from .views import exam_api_view

urlpatterns = [
    path('exam_api_view/', exam_api_view, name='exam_api_view'),
]
