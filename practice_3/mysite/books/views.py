# Create your views here.
from django.shortcuts import render_to_response
from books.models import Book
from books.models import Author
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView

def books(request):
 books = Book.objects.all()
 return render_to_response('book_list.html', {'books': books},)

def book(request, book):
 try:
  one_book = Book.objects.get(id=book)
 except ObjectDoesNotExist:
  return HttpResponse("Error, no book", content_type="text/plain")
 return render_to_response('book.html', {'book': one_book},)
def authors(request):
 authors = Author.objects.all()
 return render_to_response('author_list.html', {'authors': authors},)
def author(request, author):
 try:
  one_author = Author.objects.get(id=author)
 except ObjectDoesNotExist:
  return HttpResponse("Error, no author", content_type="text/plain")
 return render_to_response('author.html', {'author': one_author},)



class BookList(ListView):
	model = Book
	context_object_name = 'books'

class AuthorList(ListView):
	model = Author
	context_object_name = 'authors'

class BooksDetail(DetailView):
	model = Book
	context_object_name = 'books'

class AuthorsDetail(DetailView):
	model = Author
	context_object_name = 'authors'
