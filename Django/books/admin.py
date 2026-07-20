from django.contrib import admin
from .models import Books, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    fk_name = 'book'
    extra = 1


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user', 'created_at']
    search_fields = ['title', 'author']
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating']
    list_filter = ['rating']
