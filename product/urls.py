from django.urls import path
from .views import ProductCreatedView, ProductListViewByStore, ProductUpdatedView
urlpatterns = [
    path('store/',ProductCreatedView.as_view(), name='create-product'),
    path('index/', ProductListViewByStore.as_view(), name='get-product' ),
    path('<int:pk>/update/', ProductUpdatedView.as_view(), name='updated -product' )
]