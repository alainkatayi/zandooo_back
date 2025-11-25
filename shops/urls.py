from django.urls import path
from .views import ShopCreatedView, ShopUpdatedView, ShopOneView

urlpatterns = [
    path('store/', ShopCreatedView.as_view(), name='create_store'),
    path('<int:pk>/update/', ShopUpdatedView.as_view(), name='update_store'),
    path('<int:pk>/show/', ShopOneView.as_view(), name='one_store'),
]