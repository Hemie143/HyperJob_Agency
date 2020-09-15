from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ['review1', 'reviews2']  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        context = dict(reviews=self.reviews)
        return render(request, 'book/reviews.html', context=context)
