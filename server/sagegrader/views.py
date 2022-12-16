from django.shortcuts import render
from rest_framework import generics
from .models import Institution, User
from .serializers import InstitutionSerializer, UserSerializer, UserUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend

class InstitutionView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class InstitutionViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    fieldset_fields = ['user_role']  # User tablosunda user_role göre filtreleme yapılır.
    filter_backends = [DjangoFilterBackend]  # tüm alanlara filtreleme yapmaya yarar.

class UserViewRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
