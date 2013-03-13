from django.db import models
from mezzanine.pages.models import Page

class Author(Page):
    dob=models.DateField("date of birth")

class Book(models.Model):
    author=models.ForeignKey("Author")
    cover=models.ImageField(upload_to="authors")

# Create your models here.
