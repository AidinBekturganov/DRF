from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author', 'phone', 'price', 'address', 'year', 'area')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)