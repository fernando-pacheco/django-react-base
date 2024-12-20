import uuid
from django.db import models


class BaseUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)


class BaseIntModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    base_uuid = models.ForeignKey(BaseUUIDModel, on_delete=models.CASCADE)
