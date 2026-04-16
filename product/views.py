from django.shortcuts import render, get_object_or_404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Product


# Class pour la création d'un produits
class ProductCreatedView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            product = serializer.save(shop=request.user.shop)
            return Response({
                "Message":"Product created successfully",
                "Product": ProductSerializer(product).data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


# class pour la liste des produits d'une boutique
class ProductListViewByStore(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if hasattr(request.user,'shop'):
            product = request.user.shop.store.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)
        else:
            return Response({
                "Erreur": "Aucune boutique ou Produit associée à cet utilisateur."
            })
        