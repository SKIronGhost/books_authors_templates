from django.urls import path
from . import views

urlpatterns = (
    path('', views.index),
    path('books', views.render_books),
    path('authors', views.render_authors),
    path('new_book', views.new_book),
    path('new_author', views.new_author),
    path('books/<str:book_id>', views.book_view),
    path('authors/<str:author_id>', views.author_view),
    path('books/<str:book_id>/add_author', views.add_author_in_books),
    path('authors/<str:author_id>/add_book', views.add_book_in_authors),
)
