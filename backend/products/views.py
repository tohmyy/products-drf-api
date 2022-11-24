from ast import arg
from re import A
from tkinter import PROJECTING
from django.http import HttpResponse
from django.shortcuts import render
from requests import request

from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.mixins import (UserQuerySetMixin, StaffEditorPermissionMixin)

# from django.http import Http404

from django.shortcuts import get_object_or_404

from .permissions import IsStaffEditorPermission

from .models import Product

from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #custom mixin can also be used to import these permissions

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)


    #you can even substitute this whole function by importing a custom mixin for get_querysets
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=request.user)


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)



#   #using function-based views instead of generic views
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
    
#     if method=='GET':
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)


#         qs = Product.objects.all()
#         data = ProductSerializer(qs, many=True).data
#         return Response(data)


#     if method=='POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.validated_data)
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)

#             print(serializer.data)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)








class ProductRetrieveUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateAPIView):
    allow_staff_view = False
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content =  instance.title


class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# Create your views here.
