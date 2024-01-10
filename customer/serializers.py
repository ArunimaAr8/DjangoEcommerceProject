from rest_framework import serializers


class CustomerSignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    mobile = serializers.IntegerField()
    email = serializers.IntegerField()
    password = serializers.CharField(max_length=100)
