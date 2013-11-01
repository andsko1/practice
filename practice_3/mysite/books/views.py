# Create your views here.
from django.shortcuts import render_to_response
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

def books(request):
 books = Book.objects.all()
 return render_to_response('book_list.html', {'books': books},)

def book(request, book):
 try:
  one_book = Book.objects.get(id=book)
 except ObjectDoesNotExist:
  return HttpResponse("Error, no book", content_type="text/plain")
 return render_to_response('book.html', {'book': one_book})
