from django.contrib import admin
from store.models import Product, Category

class Products(admin.ModelAdmin):
    list_display = ('name','description','value','category','img_url','creation_date','last_update',)
    list_display_links = ('name','category','value',)
    list_per_page = 20
    search_fields = ('name','category', 'value',)


admin.site.register(Product, Products)

class Categorys(admin.ModelAdmin):
    list_display = ('name','description','creation_date','last_update',)
    list_display_links = ('name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Category, Categorys)




