from django.shortcuts import render, get_object_or_404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.generics import ListAPIView
from .pagination import ProductPagination


# Class pour la création d'un produits
class ProductCreatedView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if hasattr(request.user,'shop'):
                
            if serializer.is_valid():
                product = serializer.save(shop=request.user.shop)
                return Response({
                    "Message":"Product created successfully",
                    "Product": ProductSerializer(product).data
                },status=status.HTTP_201_CREATED)
                
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "Erreur": "Vous n'avez pas de boutique. Veuiller ouvri une boutique pour commencer"
            }, status= status.HTTP_401_UNAUTHORIZED)

# class pour la modification d'un produit
class ProductUpdatedView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        owner = product.shop.owner
        if owner != request.user:
            return Response({
                "Message":"You do not have the right to modify this product information",
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = ProductSerializer(product, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Message": "Product modified successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "Error" : serializer.errors
                }, status=status.HTTP_200_OK)

class ProductDeletedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        owner = product.shop.owner
        if owner != request.user:
            return Response({
                "Message": "You do not have the right to delete this product"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            product.delete()
            return Response({
                "Message":"Product deleted"
            }, status=status.HTTP_204_NO_CONTENT)


# class pour la liste des produits d'une boutique
class ProductListViewByStore(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if hasattr(request.user,'shop'):
            product = request.user.shop.store.all()
            serializer = ProductSerializer(product, many=True)
            if len(product) == 0:
                return Response({
                    "Message": "Aucun produit dans votre boutique"
                })
            return Response(serializer.data)
        else:
            return Response({
                "Erreur": "Aucune boutique ou Produit associée à cet utilisateur."
            })

#class pour recuperer tout les produits disponible sur dans la bd
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
        