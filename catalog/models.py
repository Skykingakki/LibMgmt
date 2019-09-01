from django.db import models

# Create your models here.
from django.urls import reverse

#model for genre
class Genre(models.Model):
    name=models.CharField(max_length=5,help_text="Enter the book code(HI,HO,EE,EM,etc)")

    def __str__(self):
        return self.name

#model for language
class Language(models.Model):
    name = models.CharField(max_length=10,help_text="enter the lanuage of the book(hindi,english,etc)")

    def __str__(self):
        return self.name

#model for author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # generating link
        return reverse('author-detail',args=[str(self.id)])


#model for book
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    isbn=models.CharField('ISBN',max_length=6,help_text="enter a 5 bit number")
    genre=models.ForeignKey('Genre',on_delete=models.SET_NULL,null=True)
    language=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])

    #####display_genre

import uuid
from datetime import date
from django.contrib.auth.models import User

class BookInstance(models.Model):
    id=models.CharField(max_length=20,primary_key=True,help_text="enter a unique id for this particular book")
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    issued_on=models.DateField(null=True,blank=True)
    due_back = models.DateField(null=True, blank=True)
    borrower=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today()>self.due_back:
            return True
        return False

    LOAN_STATUS=(
            ('d','Not available'),
            ('o','on Loan'),
            ('a','Available'),
            ('r','reserved')
        )

    status=models.CharField(max_length=1,choices=LOAN_STATUS,default='a',blank=True,help_text="book availblity")

    def __str__(self):
        return (str(self.id))

