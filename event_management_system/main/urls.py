from django.urls import path
from .views import *

urlpatterns = [
    # GET: List all categories
    # POST: Create a new category
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),

    # GET: Retrieve details of a specific category
    # DELETE: Delete a specific category
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    # GET: List all events
    # POST: Create a new event
    path('events/', EventListCreateAPIView.as_view(), name='event_list_create'),

    # GET: Retrieve details of a specific event
    # PUT: Update an event (partially or fully)
    # DELETE: Delete a specific event
    path('events/<int:event_id>/', EventDetailAPIView.as_view(), name='event_detail'),

    # GET: Fetch event statistics based on pending counts
    path('event-chart/', EventChartAPIView.as_view(), name='event_chart'),
]