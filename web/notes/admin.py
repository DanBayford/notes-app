from django.contrib import admin
from .models import NoteModel


class NoteAdmin(admin.ModelAdmin):
    model = NoteModel
    list_display = ["title", "author", "get_tags", "last_edited", "is_archived"]
    search_fields = ["title", "tags__name"]

    def get_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    get_tags.short_description = "Tags"


admin.site.register(NoteModel, NoteAdmin)
