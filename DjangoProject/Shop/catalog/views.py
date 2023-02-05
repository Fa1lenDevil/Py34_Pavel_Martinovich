from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre
from django.db.models import Q


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        books = Book.objects.all()
        genres = Genre.objects.all()

        params = {
            'title': "All",
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)
        genres = Genre.objects.all()

        params = {
            'title': f"About {book.title}",
            'book': book,
            'genres': genres
        }

        return render(request, self.template_name, params)


class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"

    def get(self, request):
        authors = Author.objects.all()
        genres = Genre.objects.all()

        params = {
            'authors': authors,
            'genres': genres
        }

        return render(request, self.template_name, params)


class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        genres = Genre.objects.all()

        params = {
            'title': f"{last_name}'s",
            'author': author,
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = 'catalog/catalog.html'

    def post(self, request):
        search = request.POST['search']
        genres = Genre.objects.all()
        books_by_title = Book.objects.filter(Q(title__icontains=search) |
                                             Q(price__icontains=search) |
                                             Q(publication_date__icontains=search) |
                                             Q(summary__icontains=search) |
                                             Q(author__last_name__icontains=search) |
                                             Q(author__first_name__icontains=search))



        params = {
            'books': books_by_title,
            'title': f"'{search}'",
            'genres': genres
        }

        return render(request, self.template_name, params)

class GenreCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, id):
        genre = Genre.objects.get(id=id)
        books = Book.objects.filter(genre=genre)
        genres = Genre.objects.all()

        params = {
            'title': f"{genre.name}'s",
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)