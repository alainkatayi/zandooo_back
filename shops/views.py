from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ShopSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Shop

# Create your views here.
class ShopCreatedView(APIView):
    permission_classes  = [IsAuthenticated]

    def post(self,request):
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