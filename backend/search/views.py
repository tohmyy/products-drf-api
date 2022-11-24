from django.shortcuts import render
from requests import request

from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from . import client

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
            #defaults to filtering by current user (only current user data is displayed) 
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0" #sets default public value to false
        tag = request.GET.get('tag') or None #gets the 'tag' filter keyword from the html url
        print(user, query, public, tag)
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)


class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all() #here
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        #what this does is call the default queryset value that is above
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results

# Create your views here.
