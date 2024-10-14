from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields=('title',)
admin.site.register(Category,CategoryAdmin)