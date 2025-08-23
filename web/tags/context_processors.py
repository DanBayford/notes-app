from .models import TagModel


def all_active_tags(request):
    tags = TagModel.objects.filter(notes__is_archived=False).distinct()
    return {"all_active_tags": tags}
