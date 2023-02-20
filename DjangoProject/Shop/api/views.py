from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre
from cart.models import Cart


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]