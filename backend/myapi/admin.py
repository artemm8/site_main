
from django.contrib import admin
from .models import Category,Product,Review
from mptt.admin import MPTTModelAdmin

class CustomeMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent=30

admin.site.register(Category,CustomeMPTTModelAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("title","category",)
    prepopulated_fields={"slug":("title",)}
    search_field=("title",)
    list_filter=("category",)
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=("name","product","rating",)
    