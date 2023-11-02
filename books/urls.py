from django.urls import path
from books import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="list"),
    path("<int:book_id>/", views.BookDetailView.as_view(), name="detail"),
    path("<int:book_id>/delete", views.delete, name="delete"),
    # path("author/create/", views.create_author, name ="create-authors"),
    path("create/", views.BookCreateView.as_view(), name ="create-book"),
    path("<int:book_id>update/",  views.BookUpdateView.as_view(), name="update-book"),
]