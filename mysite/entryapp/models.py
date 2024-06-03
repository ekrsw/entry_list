from django.db import models


class EntryModel(models.Model):
    title = models.CharField(max_length=50)
    entry_text = models.CharField(max_length=500)

    def __str__(self):
        return self.title
