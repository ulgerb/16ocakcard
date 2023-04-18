from django.contrib import admin
from .models import *

admin.site.register(Category)

admin.site.register(ContactModel)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

    list_display = ('title','date_now', 'author', 'brand', 'category')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('card','name', 'date_now', 'id')
    
