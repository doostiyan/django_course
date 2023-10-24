from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book


def books_list(request):
    books = Book.objects.all()

    return render(request, "books/list.html", {"books": books})


# Create your views here.

def detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, template_name="books/detail.html", context={"book": book})


def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id),
    Book.objects.get(pk=book_id).delete()

    messages.success(request, f"Book '{book_id}' deleted successfully.", extra_tags="alert alert-success")

    return redirect("books:list")
