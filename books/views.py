from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from books.models import Books, Review
from books.forms import BookForm, ReviewForm


def book_list(request):
    books = Books.objects.select_related('added_by').annotate(
        avg_rating=Avg('review__rating')
    ).order_by('-created_at')

    return render(request, 'books/book_list.html', {
        'books': books
    })


def book_details(request, pk):
    book = get_object_or_404(Books, pk=pk)

    reviews = book.review.select_related('user').order_by('-created_at')

    avg_rating = reviews.aggregate(
        avg_rating=Avg('rating')
    )['avg_rating']

    return render(request, 'books/book_details.html', {
        'book': book,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })


@login_required
def add_review(request, pk):
    book = get_object_or_404(Books, pk=pk)

    form = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_details', pk=pk)

    return render(request, 'books/add_review.html', {
        'form': form,
        'book': book,
    })


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
    