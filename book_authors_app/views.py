from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    return render(request, "index.html")


def new_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect("/books")


def new_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")


def render_books(request):
    context = {
        "books": Book.objects.all().values(),
    }
    return render(request, "books.html", context)


def render_authors(request):
    context = {
        "authors": Author.objects.all().values(),
    }
    return render(request, "authors.html", context)


def book_view(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_book.authors.all().order_by("id")
    print(this_book.authors.all())
    actual_authors = []
    options = []

    for author in this_book.authors.values():
        actual_authors.append(author["id"])
    actual_authors.sort()

    for author in Author.objects.all():
        print("first_for", author.id)
        if actual_authors:
            for author_id in actual_authors:
                print("second_for", author_id)
                if author_id == author.id:
                    print(author.id, author_id)
                    actual_authors.pop(0)
                    break
                else:
                    options.append(author)
                    break
        else:
            options.append(author)

    context = {
        "book": this_book,
        "option": options
    }
    return render(request, "book_desc.html", context)


def author_view(request, author_id):

    this_author = Author.objects.get(id=author_id)
    actual_books = []
    options = []

    for book in this_author.books.values():
        actual_books.append(book["id"])
    actual_books.sort()

    for book in Book.objects.all():
        print("first_for", book.id)
        if actual_books:
            for book_id in actual_books:
                print("second_for", book_id)
                if book_id == book.id:
                    print(book.id, book_id)
                    actual_books.pop(0)
                    break
                else:
                    options.append(book)
                    break
        else:
            options.append(book)
    print(options)

    context = {
        "author": this_author,
        "option": options
    }
    return render(request, "author_desc.html", context)


def add_author_in_books(request, book_id):
    this_book = Book.objects.get(id=book_id)
    serial = request.POST['author_choice'].split()
    author_selected = Author.objects.filter(first_name=serial[0], last_name=serial[1])
    for author in author_selected:
        author_selected = author
    this_book.authors.add(author_selected)
    return redirect("/books")


def add_book_in_authors(request, author_id):
    this_author = Author.objects.get(id=author_id)
    book_selected = Book.objects.filter(title=request.POST['book_choice'])
    for book in book_selected:
        book_selected = book
    this_author.books.add(book_selected)
    return redirect("/authors")
