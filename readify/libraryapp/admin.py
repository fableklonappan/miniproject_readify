from django.contrib import admin
from .models import AddBook,Book,Wishlist

# Register your models here.

admin.site.register(AddBook)
admin.site.register(Book)
admin.site.register(Wishlist)