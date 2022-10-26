from django.db import models

from .ad import Ad
from users.models import User
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    text = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
        ordering = ['created_at']

    def __str__(self):
        return self.text
