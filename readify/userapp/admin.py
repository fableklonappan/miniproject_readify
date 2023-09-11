from django.contrib import admin
from.models import CustomUser
from .models import BookCategory
from .models import UserProfile


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BookCategory)
admin.site.register(UserProfile)