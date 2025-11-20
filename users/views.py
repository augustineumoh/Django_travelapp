from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from .permissions import IsAdmin



class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[permissions.AllowAny]


class LoginView(TokenObtainPairView):
    permission_classes=[permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAdmin]
# Create your views here.
