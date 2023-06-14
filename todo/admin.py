from django.contrib import admin
from .models import Category, Note


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    verbose_name_plural = "Categories"


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "category", "user", "created_at")
    verbose_name_plural = "Notes"
