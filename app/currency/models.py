from django.db import models


# Create your models here.
class UserRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    bid = models.FloatField(null=True, blank=True)
    ask = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.pk} -- {self.created_at.date()}"
