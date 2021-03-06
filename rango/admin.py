from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url','views')
    


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes')
    
    
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)