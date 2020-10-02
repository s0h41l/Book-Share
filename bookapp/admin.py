from django.contrib import admin
from .models import Profile, Book, LookUp, Friend, BookShare
# Register your models here.

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(LookUp)
admin.site.register(Friend)
admin.site.register(BookShare)

