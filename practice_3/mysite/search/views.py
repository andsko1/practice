# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from search.models import SearchBookForm
from books.models import Book

def search(request):
    books = Book.objects.all()
    books = None
    if request.method == 'POST':
        form = SearchBookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            book__isbn = form.cleaned_data['ISBN']
            if book_name:
                books = Book.objects.filter(title=book_name)
            elif book_isbn:
                books = Book.objects.filter(isbn=form_isbn)
            form.save()
    else:
        form = SearchBookForm()
    return render(request, "search/book_search.html", {'form': form, 'books': books})
