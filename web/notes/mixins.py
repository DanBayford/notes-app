from tags.models import TagModel


class TagProcessingMixin:
    """
    A mixin to help handle Note Tag formatting
    """

    def get_context_data(self, **kwargs):
        """
        Formats / persists the string representation of a Notes Tags
        """
        ctx = super().get_context_data(**kwargs)

        # Check if called via form_invalid, and persist tag string if so
        if "submitted_tag_string" in kwargs:
            ctx["tag_string"] = kwargs.get("submitted_tag_string")
        # Othewise create tag string from model instance
        elif self.object:
            tag_queryset = self.object.tags.all()
            ctx["tag_string"] = ", ".join(tag.name for tag in tag_queryset)

        return ctx

    def update_tags(self, tags, note):
        """
        Updates the Tags on a Note instance
        """
        updated_tags = []
        for tag in tags:
            tag, created = TagModel.objects.get_or_create(name=tag)
            updated_tags.append(tag)

        # Update note instance
        note.tags.set(updated_tags)

        # Clean any orphaned Tag instances
        TagModel.objects.filter(notes=None).delete()
