from tabnanny import verbose
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return F"title: {self.title}"

    class Meta:
        verbose_name_plural  = "Blogs"