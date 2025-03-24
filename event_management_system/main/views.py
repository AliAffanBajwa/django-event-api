from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer

# Category API Views
class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        if category.event_set.exists():
            return Response({"error": "You cannot delete this category as it contains events."}, status=status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response({"message": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Event API Views
class EventListCreateAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailAPIView(APIView):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
        return Response({"message": "Event deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Event Statistics API
class EventChartAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        pending_counts = {
            category.name: Event.objects.filter(category=category, start_date__gt=timezone.now()).count()
            for category in categories
        }
        return Response(pending_counts)
