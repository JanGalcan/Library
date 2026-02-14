from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "nationality")
    search_fields = ("first_name", "last_name")
    list_filter = ("nationality",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published_year", "genre")
    search_fields = ("title",)
    list_filter = ("genre", "published_year")
