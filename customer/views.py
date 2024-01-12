from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import *
from .models import *


# Customer Signup API(POST API) Starts here
class CustomerSignup(APIView):
    def post(self, request):
        try:
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
                    username_id=username,  # -----> foreign key should be given as "_id"
                    mobile=mobile,
                    email=email,
                    password=password
                )
                message = {"Message": "Customer Signup Successful"}
                return JsonResponse(message, status=status.HTTP_201_CREATED, safe=False)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
        except Exception as e:
            message = {"Message": str(e)}
            return JsonResponse(message, status.HTTP_400_BAD_REQUEST)


# Customer Login API(POST API) Starts here
class CustomerLogin(APIView):
    def post(self, request):
        try:
            serializer = CustomerLoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                password = serializer.data["password"]
                loginData = list(CustomerData.objects.filter(
                    username=username, password=password).values())
                if len(loginData) == 1:
                    message = {"Message": "Login Successful"}
                    return JsonResponse(message, status=status.HTTP_200_OK)
                else:
                    message = {"Message": "Invalid Credentials"}
                    return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {"Message": str(e)}
            return JsonResponse(message, status.HTTP_400_BAD_REQUEST)