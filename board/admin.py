from django.contrib import admin
from board.models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=( 'title','content','price')
    