from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


@admin.register(Castle, Unit)
class CastleUnitAdmin(admin.ModelAdmin):
    prepopulated_fields = ({'slug': ('title',)})


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")
    list_editable = ("is_published",)
