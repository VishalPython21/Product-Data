from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView,TopProductsAllTogetherView, TopProductsLastDayView, TopProductsLastWeekView
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
    path('top-products/all-together/', TopProductsAllTogetherView.as_view(), name='top-products-all-together'),
    path('top-products/last-day/', TopProductsLastDayView.as_view(), name='top-products-last-day'),
    path('top-products/last-week/', TopProductsLastWeekView.as_view(), name='top-products-last-week'),

]