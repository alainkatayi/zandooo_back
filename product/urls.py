from django.urls import path
from .views import ProductCreatedView, ProductListViewByStore, ProductUpdatedView, ProductDeletedView
urlpatterns = [
    path('store/',ProductCreatedView.as_view(), name='create-product'),
    path('index/', ProductListViewByStore.as_view(), name='get-product' ),
    path('<int:pk>/update/', ProductUpdatedView.as_view(), name='updated -product' ),
    path('<int:pk>/delete/', ProductDeletedView.as_view(), name='deleted-product' )
]