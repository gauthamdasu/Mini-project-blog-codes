from django.db import models


class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
