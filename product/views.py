from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
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
        