import pytest
import os
from main import Library

@pytest.fixture
def library():
    test_file = 'test_library.json'
    lib = Library(test_file)
    yield lib
    os.remove(test_file)

def test_add_book(library):
    book = library.add_book("Test Book", "Test Author", "2024")
    assert book in library.books
    assert book['title'] == "Test Book"
    assert book['author'] == "Test Author"
    assert book['year'] == "2024"
    assert book['status'] == "в наличии"

def test_delete_book(library):
    book = library.add_book("Test Book", "Test Author", "2024")
    book_id = book['id']
    result = library.delete_book(book_id)
    assert result
    assert book not in library.books

def test_search_books(library):
    book = library.add_book("Unique Book", "Unique Author", "2024")
    results = library.search_books('title', 'Unique Book')
    assert book in results

def test_change_status(library):
    book = library.add_book("Test Book", "Test Author", "2024")
    book_id = book['id']
    result = library.change_status(book_id, 'выдана')
    assert result
    assert library.books[0]['status'] == 'выдана'

def test_display_books(library):
    library.add_book("Book1", "Author1", "2023")
    library.add_book("Book2", "Author2", "2024")
    books = library.display_books()
    assert len(books) == 2
    assert books[0]['title'] == "Book1"
    assert books[1]['title'] == "Book2"
