from asyncore import read
from rest_framework import serializers


#all attributes of the current user can now be displayed by using a different class or method get
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only= True)
    password = serializers.CharField(read_only=True)