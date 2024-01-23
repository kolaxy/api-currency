from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
import requests
import json

from rest_framework import generics
from .serializers import UserRequestSerializer
from .models import UserRequest


from .utils import create_user_request


from rest_framework.response import Response
from rest_framework import status


class UserRequestListView(generics.ListAPIView):
    queryset = UserRequest.objects.all()[:10]
    serializer_class = UserRequestSerializer

    def list(self, request, *args, **kwargs):
        url = "https://economia.awesomeapi.com.br/last/USD-RUB"
        headers = {"Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
        current_exchange_rate = json.loads(response.text)["USDRUB"]
        queryset_serializer = self.get_serializer(self.get_queryset(), many=True)
        response_data = {
            "current_exchange_rate": current_exchange_rate,
            "history": queryset_serializer.data,
        }
        create_user_request()
        return Response(response_data, status=status.HTTP_200_OK)
