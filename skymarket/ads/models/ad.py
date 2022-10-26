from django.db import models

from users.models import User
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    title = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True)
    image = models.ImageField(upload_to="django_media/", null=True)

    class Meta:
        verbose_name = _("Объявление")
        verbose_name_plural = _("Объявления")
        ordering = ['created_at']

    def __str__(self):
        return self.title
