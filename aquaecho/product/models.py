from django.db import models


# Create your models here.
class AcessLog(models.Model):
    method = models.CharField(max_length=127)
    host = models.CharField(max_length=255)
    full_path_info = models.TextField()
    scheme = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, blank=True)
    meta_data = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
