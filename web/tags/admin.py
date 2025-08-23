from django.contrib import admin
from .models import TagModel


class TagAdmin(admin.ModelAdmin):
    model = TagModel
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(TagModel, TagAdmin)
