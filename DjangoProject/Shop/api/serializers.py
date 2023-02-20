from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre
from cart.models import Cart


class BookSerializer(serializers.ModelSerializer):
    author_last_name = serializers.ReadOnlyField(source='author.first_name')

    class Meta:
        model = Book
        fields = ['title', 'author_last_name', 'summary', 'publication_date', 'price', 'amount', 'genre', 'author', 'image', 'get_genre']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'photo']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'display_products', 'get_total_price', 'get_total_quantity']
