import uuid
from django.db import models
from users.models import CustomUser


class TagModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tags", null=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
