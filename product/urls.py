from django.urls import path
from .views import ProductCreatedView
urlpatterns = [
    path('store/',ProductCreatedView.as_view(), name='create-product')
]