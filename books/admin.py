from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "author"]

    list_filter = ["author", "publication_date"]
    list_per_page = 2

    fields = (
        (None, {"fields": ["title", "author", "price", "description",]}),
        ("Other fields", {"fields": ["publication_data", "cover"]})
    )

admin.site.register(Book, BookAdmin)
# admin.site.register(Author)

# Register your models here.
