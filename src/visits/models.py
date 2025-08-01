from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
class PageVisit(models.Model):
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateTimeField(auto_now_add=True)
    # subdomain = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)