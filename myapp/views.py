from rest_framework import generics, status
from django.utils import timezone
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from datetime import timedelta


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Record successfully deleted."}, status=status.HTTP_200_OK)


class TopProductsAllTogetherView(generics.ListAPIView):
    queryset = Product.objects.annotate(retrieval_count=Count('retrieved_count')).order_by('-retrieval_count')[:5]
    serializer_class = ProductSerializer

class TopProductsLastDayView(generics.ListAPIView):
    queryset = Product.objects.filter(last_retrieved_at__gte=timezone.now() - timedelta(days=1)).annotate(last_day_retrieval_count=Count('retrieved_count')).order_by('-last_day_retrieval_count')[:5]
    serializer_class = ProductSerializer

class TopProductsLastWeekView(generics.ListAPIView):
    queryset = Product.objects.filter(last_retrieved_at__gte=timezone.now() - timedelta(weeks=1)).annotate(last_week_retrieval_count=Count('retrieved_count')).order_by('-last_week_retrieval_count')[:5]
    serializer_class = ProductSerializer