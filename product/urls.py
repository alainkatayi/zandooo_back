from django.urls import path
from .views import ProductCreatedView, ProductListView
urlpatterns = [
    path('store/',ProductCreatedView.as_view(), name='create-product'),
    path('index/', ProductListView.as_view(), name='get-product' )
]