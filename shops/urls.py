from django.urls import path
from .views import ShopCreatedView, ShopUpdatedView

urlpatterns = [
    path('store/', ShopCreatedView.as_view(), name='create_store'),
    path('<int:pk>/update/', ShopUpdatedView.as_view(), name='update_store'),
]