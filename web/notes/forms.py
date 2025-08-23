from django import forms
from .models import NoteModel


class NotesForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Add tags seperated by commas (e.g. Work, Planning)"}
        ),
    )

    class Meta:
        model = NoteModel
        fields = ("title", "content")

    def clean_tags(self):
        data = self.cleaned_data.get("tags")

        # Empty tag string
        if not data:
            raise forms.ValidationError("Please enter at least one tag")

        tags_list = [tag.strip() for tag in data.split(",") if tag.strip()]

        # Check if any invalid values exist after processing
        if len(tags_list) < 1:
            raise forms.ValidationError("Please enter at least one tag")

        # Check for any too large tags
        invalid_tags = [tag for tag in tags_list if len(tag) > 20]
        if invalid_tags:
            raise forms.ValidationError(
                f"The following tags are too long: {', '.join(invalid_tags)}"
            )

        # Return the validated list of tags
        return tags_list
