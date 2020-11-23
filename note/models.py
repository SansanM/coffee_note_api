from django.db import models
import uuid
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Note(models.Model):
    uuid  = models.UUIDField('uuid', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="タイトル", max_length=100)
    body  = models.TextField('本文',default="")
    sanmi = models.IntegerField("酸味",validators=[MinValueValidator(1), MaxValueValidator(10)])
    nigami = models.IntegerField("苦味",validators=[MinValueValidator(1), MaxValueValidator(10)])
    like =  models.IntegerField("評価",validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public =models.BooleanField(verbose_name='公開',default=False,)
    created_at = models.DateTimeField("追加日時",auto_now_add=True)
    updated_at = models.DateTimeField("更新日時",auto_now=True)