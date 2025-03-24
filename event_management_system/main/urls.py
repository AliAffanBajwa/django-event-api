from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('events/', EventListCreateAPIView.as_view(), name='event_list_create'),
    path('events/<int:event_id>/', EventDetailAPIView.as_view(), name='event_detail'),
    path('event-chart/', EventChartAPIView.as_view(), name='event_chart'),
]
