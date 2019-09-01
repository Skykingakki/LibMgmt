from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language


admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    display = ('name')
    fields = ['name']
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'issued_on','due_back', 'id')
    list_filter = ('status', 'issued_on','due_back')

    fieldsets = (
        (None, {
            'fields': ('book','id')
        }),
        ('Availability', {
            'fields': ('status','issued_on','due_back', 'borrower')

        }),
    )

# Register your models here.
