"""
Menu Model
"""
from users.models import User
from django.db import models


class Menu(models.Model):
    """
    Menu model class
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    # user = models.ForeignKey('users.User', related_name='menu', on_delete=models.CASCADE, null=False)
    benefit = models.TextField(blank=False, null=False)

    class Meta:
        """
        Menu Meta data
        """
        ordering = ('created',)
