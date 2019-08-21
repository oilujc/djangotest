from app.models import (Book, Section)
# from pages.models import (Page,)

# The context processor function
def books(request):
	all_books = Book.objects.all()

	return {
        'books': all_books,
	}

def sections(request):
	all_sections = Section.objects.all()

	return {
        'sections': all_sections,
	}
