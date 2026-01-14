from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ShopSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Shop
from rest_framework.generics import ListAPIView
from .pagination import ShopPagination
from rest_framework.decorators import action
from rest_framework import viewsets, status
# Create your views here.
class ShopCreatedView(APIView):
    permission_classes  = [IsAuthenticated]

    def post(self,request):
        # on verifie si l'utilisateur possede deja une boutique
        if hasattr(request.user,'shop'):
            return Response({
                "Erreur": "Vous ne pouvez pas avoir plus d'une boutique",
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            shop = serializer.save(owner=request.user)
            return Response({
                "Message":"Shop created successfully",
                "Shop": ShopSerializer(shop).data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopUpdatedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self,request,pk):
        shop = get_object_or_404(Shop, pk=pk)
        if shop.owner != request.user:
            return Response({
                "Message": "You do not have the right to modify this shop information"
            }, status= status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = ShopSerializer(shop, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message":"Shop modified successfully"
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    "Error": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
class ShopOneView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,pk):
        shop = get_object_or_404(Shop,pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
    
class ShopDeletedView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        shop =get_object_or_404(Shop, pk=pk)
        if shop.owner != request.user:
            return Response({
                "Message": "You do not have the right to delete this shop."
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            shop.delete()
            return Response({
                "Message":"Shop deleted"
            },status=status.HTTP_204_NO_CONTENT)
        
class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = ShopPagination