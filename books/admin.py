from django.contrib import admin
from .models import Book, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    fk_name = 'book'
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'added_by', 'created_at']
    search_fields = ['title', 'author']
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating']
    list_filter = ['rating']
