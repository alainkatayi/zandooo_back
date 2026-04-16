from django.urls import path
from .views import ProductCreatedView, ProductListViewByStore
urlpatterns = [
    path('store/',ProductCreatedView.as_view(), name='create-product'),
    path('index/', ProductListViewByStore.as_view(), name='get-product' )
]