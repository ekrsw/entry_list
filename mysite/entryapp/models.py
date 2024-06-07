from django.db import models
from accounts.models import CustomUser


class EntryModel(models.Model):
    title = models.CharField(max_length=50)
    entry_text = models.CharField(max_length=500)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
