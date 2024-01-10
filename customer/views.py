from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import *
from .models import *


class CustomerSignup(APIView):
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data["username"]
            mobile = serializer.data["mobile"]
            email = serializer.data["email"]
            password = serializer.data["password"]

            CustomerData.objects.create(
                username=username,
                mobile=mobile,
                email=email,
                password=password
            )

            Profile.objects.create(
                username_id=username,
                mobile=mobile,
                email=email,
                password=password
            )
            message = {"Message": "Customer Signup Successful"}
            return JsonResponse(message, status=status.HTTP_201_CREATED, safe=False)
