from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ShopSerializer
from rest_framework.response import Response
from rest_framework import status

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