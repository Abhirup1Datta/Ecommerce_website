from django.contrib import admin
from .models import Products,Order

admin.site.site_header = "Mithaiwala"
admin.site.site_title ='Shopping site'
admin.site.index_title ='Management Panel'


class ProductAdmin(admin.ModelAdmin):
    list_display= ('title','price','discount_price','description')
    search_fields=('title','price')
    list_editable= ('price','discount_price','description',)

# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)