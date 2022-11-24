from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home ), #localhost:8000/api
    # path('api/product', include('products.urls')) #can be used this way(it works)
]
