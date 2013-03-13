from django.contrib import admin
from copy import deepcopy

from mezzanine.pages.admin import PageAdmin

from .models import Author,Book

author_extra_fieldsets=((None,{"fields":("dob",)}),)

class BookInline(admin.TabularInline):
    model=Book
class AuthorAdmin(PageAdmin):
    inlines=(BookInline,)
    fieldsets=deepcopy(PageAdmin.fieldsets)+author_extra_fieldsets

admin.site.register(Author,AuthorAdmin)
