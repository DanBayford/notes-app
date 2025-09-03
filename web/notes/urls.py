from django.urls import path
from .views import *

app_name = "notes"

urlpatterns = [
    path("", NotesDetailView.as_view(), name="all"),
    path("<uuid:pk>/", NotesDetailView.as_view(), name="detail"),
    path("create/", NotesCreateView.as_view(), name="create"),
    path("search/", NotesSearchView.as_view(), name="search"),
    path("archived/", ArchivedNotesDetailView.as_view(), name="archived-all"),
    path(
        "archived/<uuid:pk>/", ArchivedNotesDetailView.as_view(), name="archived-detail"
    ),
    path("archive/", archive_note, name="archive"),
    path("restore/", restore_note, name="restore"),
    path("delete/", delete_note, name="delete"),
]
