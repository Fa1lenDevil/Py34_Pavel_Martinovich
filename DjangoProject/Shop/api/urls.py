from django.urls import path
from .views import UserList, GenreList, AuthorList, BookList, CartList


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='api-authors'),
    path('genres/', GenreList.as_view(), name='api-genres'),
    path('books/', BookList.as_view(), name='api-books'),
    path('users/', UserList.as_view(), name='api-users'),
    path('carts/', CartList.as_view(), name='api-carts')
]