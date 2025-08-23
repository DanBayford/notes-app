from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, CreateView, TemplateView
from django.urls import reverse
from .forms import NotesForm
from .mixins import TagProcessingMixin
from .models import NoteModel


@require_POST
def archive_note(request):
    note_id = request.POST.get("archive")

    try:
        note = NoteModel.objects.get(id=note_id)
        note.is_archived = True
        note.save()

        messages.success(request, "Note successfully archived")
        return redirect(reverse("notes:archived-detail", kwargs={"pk": note_id}))

    except NoteModel.DoesNotExist:
        messages.error(request, "Error archiving note")
        # Try and redirect to same page if HTTP_Referer header present, otherwise redirect to '/notes'
        # request.path redirects a GET to origin url, which is POST only (ie this url)
        referer = request.META.get("HTTP_REFERER", "/notes")
        return redirect(referer)


@require_POST
def restore_note(request):
    note_id = request.POST.get("restore")

    try:
        note = NoteModel.objects.get(id=note_id)
        note.is_archived = False
        note.save()

        messages.success(request, "Note successfully restored")
        return redirect(reverse("notes:detail", kwargs={"pk": note_id}))

    except NoteModel.DoesNotExist:
        messages.error(request, "Error restoring note")
        referer = request.META.get("HTTP_REFERER", "/notes")
        return redirect(referer)


@require_POST
def delete_note(request):
    note_id = request.POST.get("delete")

    try:
        note = NoteModel.objects.get(id=note_id)
        note_was_archived = note.is_archived
        note.delete()

        if note_was_archived:
            messages.success(request, "Archived note successfully deleted")
            return redirect(reverse("notes:archived-all"))

        else:
            messages.success(request, "Note successfully deleted")
            return redirect(reverse("notes:all"))

    except NoteModel.DoesNotExist:
        messages.error(request, "Error deleting note")
        referer = request.META.get("HTTP_REFERER", "/notes")
        return redirect(referer)


class NotesDetailView(TagProcessingMixin, UpdateView):
    model = NoteModel
    form_class = NotesForm
    template_name = "notes/notesDetail.html"
    context_object_name = "note"

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()

        pk = self.kwargs.get("pk")
        if pk:
            return queryset.get(pk=pk)

        return None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        params = self.request.GET.dict()

        query_filter = Q(is_archived=False)

        if "tag" in params:
            tag = params["tag"]
            query_filter &= Q(tags__name=tag)

        if "search" in params:
            search_term = params["search"]
            query_filter &= Q(title__icontains=search_term) | Q(
                tags__name__icontains=search_term
            )

        ctx["notes"] = (
            NoteModel.objects.filter(author=self.request.user)
            .filter(query_filter)
            .distinct()
        )

        return ctx

    def post(self, request, *args, **kwargs):
        # BaseUpdateView sets self.object in post
        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        # Persist tag string
        submitted_tag_string = request.POST.get("tags", "")
        return self.form_invalid(form, submitted_tag_string)

    def form_valid(self, form):
        tags = form.cleaned_data["tags"]

        note = self.get_object()

        note.title = form.cleaned_data["title"]
        note.content = form.cleaned_data["content"]
        note.author = self.request.user

        self.update_tags(tags, note)

        note.save()
        messages.success(self.request, "Note successfully updated.")
        return redirect(reverse("notes:detail", kwargs={"pk": note.pk}))

    def form_invalid(self, form, submitted_tag_string):
        return self.render_to_response(
            self.get_context_data(form=form, submitted_tag_string=submitted_tag_string)
        )


class NotesCreateView(TagProcessingMixin, CreateView):
    model = NoteModel
    form_class = NotesForm
    template_name = "notes/notesCreate.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        query_filter = Q(is_archived=False)

        ctx["notes"] = (
            NoteModel.objects.filter(author=self.request.user)
            .filter(query_filter)
            .distinct()
        )

        return ctx

    def post(self, request, *args, **kwargs):

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        submitted_tag_string = request.POST.get("tags", "")
        return self.form_invalid(form, submitted_tag_string)

    def form_valid(self, form):
        tags = form.cleaned_data["tags"]

        note = NoteModel.objects.create(
            title=form.cleaned_data["title"],
            content=form.cleaned_data["content"],
            author=self.request.user,
        )

        self.update_tags(tags, note)

        note.save()
        messages.success(self.request, "Note successfully created.")
        return redirect(reverse("notes:detail", kwargs={"pk": note.pk}))

    def form_invalid(self, form, submitted_tag_string):
        # Explicitly set self.object to None if validation fails
        # Not done by default on POST for CreateView
        self.object = None
        return self.render_to_response(
            self.get_context_data(form=form, submitted_tag_string=submitted_tag_string)
        )


class NotesListMobile(TemplateView):
    template_name = "notes/notesListMobile.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        params = self.request.GET.dict()

        query_filter = Q(is_archived=False)

        if "tag" in params:
            tag = params["tag"]
            query_filter &= Q(tags__name=tag)

        ctx["notes"] = NoteModel.objects.filter(author=self.request.user).filter(
            query_filter
        )

        return ctx


class ArchivedNotesDetailView(TagProcessingMixin, UpdateView):
    model = NoteModel
    form_class = NotesForm
    template_name = "notes/notesDetail.html"
    context_object_name = "note"

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()

        pk = self.kwargs.get("pk")
        if pk:
            return queryset.get(pk=pk)

        return None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["notes"] = NoteModel.objects.filter(author=self.request.user).filter(
            is_archived=True
        )

        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        submitted_tag_string = request.POST.get("tags", "")
        return self.form_invalid(form, submitted_tag_string)

    def form_valid(self, form):
        tags = form.cleaned_data["tags"]

        note = self.get_object()

        note.title = form.cleaned_data["title"]
        note.content = form.cleaned_data["content"]
        note.author = self.request.user

        self.update_tags(tags, note)

        note.save()
        messages.success(self.request, "Archived note successfully updated.")
        return redirect(reverse("notes:archived-detail", kwargs={"pk": note.pk}))

    def form_invalid(self, form, submitted_tag_string):
        return self.render_to_response(
            self.get_context_data(form=form, submitted_tag_string=submitted_tag_string)
        )
