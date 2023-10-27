from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from books.forms import AuthorCreateForm
from books.models import Book, Author


def books_list(request):
    books = Book.objects.all()

    return render(request, "books/list.html", {"books": books})


# Create your views here.

def detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, template_name="books/detail.html", context={"book": book})


def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    Book.objects.get(pk=book_id).delete()

    messages.success(request, f"Book '{book.title}' deleted successfully.", extra_tags="alert alert-success")

    return redirect("books:list")


def create_author(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            Author.objects.create(name=form.cleaned_data["name"], bio=form.cleaned_data["bio"])

            messages.success(request, message=f"Author '{form.cleaned_data['name']}'create successfully",
                             extra_tags="alert alert-success")
    else:
        form = AuthorCreateForm()

    return render(request, template_name="authors/create.html", context={"form": form})


def create_book(request):
    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message=f"Book '{form.cleaned_data['title']}'create successfully",
                             extra_tags="alert alert-success")

    else:
        form = BookCreateForm()

    return render(request, template_name="books/create.html", context={"form": form})


def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, message=f"Book '{form.cleaned_data['title']}'create successfully",
                             extra_tags="alert alert-success")

    else:
        form = BookCreateForm(instance=book)

    return render(request, template_name="books/update.html", context={"form": form })
