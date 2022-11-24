from django.urls import path
from . import views

# /api/products/
urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),


    # path('list/', views.ProductListAPIView.as_view()),
    path('<int:pk>/retrieve-update/', views.ProductRetrieveUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/destroy/', views.ProductDestroyAPIView.as_view()),




#------undo------
    # path('', views.ProductMixinView.as_view()),
    # path('<int:pk>/', views.ProductMixinView.as_view()),


    # # path('list/', views.ProductListAPIView.as_view()),
    # path('<int:pk>/update/', views.ProductMixinView.as_view()),
    # path('<int:pk>/destroy/', views.ProductDestroyAPIView.as_view()),
]

#   #using function-based views instead of generic views
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
    # path('list/', views.product_alt_view),