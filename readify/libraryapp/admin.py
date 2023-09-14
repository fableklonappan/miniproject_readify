from django.contrib import admin
from .models import AddBook,BookCart,Wishlist,AudioBook

# Register your models here.

admin.site.register(AddBook)
admin.site.register(BookCart)
admin.site.register(Wishlist)
admin.site.register(AudioBook)