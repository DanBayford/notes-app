from .models import TagModel


def all_active_tags(request):
    if request.user.is_authenticated:
        tags = TagModel.objects.filter(notes__is_archived=False, user=request.user).distinct()
    else:
        tags = None
    return {"all_active_tags": tags}
