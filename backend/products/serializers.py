from cgitb import lookup
import imp
from requests import request

from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from . import validators

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.SerializerMethodField(read_only=True)

    owner = UserPublicSerializer(source='user', read_only=True)

    ceo = serializers.SerializerMethodField(read_only=True)

    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.HyperlinkedIdentityField(
                view_name='product-update',
                lookup_field='pk',
    )
    title = serializers.CharField(validators=[validators.validate_title, validators.unique_product_title])

    class Meta:
        model = Product
        fields = [
            # 'user',
            'ceo',
            'owner',
            'url',
            'update_url',
            # 'email',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'public',
            'path',
            'pk',
        ]


#all attributes of the current user can now be displayed by using a different class or method get here
    def get_ceo(self, obj):
        return{
            "username": obj.user.username,
            "id": obj.user.id,
            "email": obj.user.email,
        }

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already an existing product name")
    #     return value

    # email = serializers.EmailField(write_only=True)

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)


    def get_my_discount(self, obj): #looking for get_my_discount (from my_discount field)
        if not hasattr(obj, 'id'): 
            return None
        if not isinstance(obj, Product): #if there's no instance
            return None
        return obj.get_discount() #will now return it from models.py