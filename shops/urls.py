from django.urls import path
from .views import ShopCreatedView

urlpatterns = [
    path('store/', ShopCreatedView.as_view(), name='create_store'),
]