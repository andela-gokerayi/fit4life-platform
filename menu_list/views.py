from menu_list.models import Menu
from menu_list.serializers import MenuSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import get_user
 
class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def perform_create(self, serializer):
        serializer.save()
 
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all().filter(user=self.request.user)
