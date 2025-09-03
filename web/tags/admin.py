from django.contrib import admin
from .models import TagModel


class TagAdmin(admin.ModelAdmin):
    model = TagModel
    list_display = ["name", "user"]
    search_fields = ["name", "user"]


admin.site.register(TagModel, TagAdmin)
