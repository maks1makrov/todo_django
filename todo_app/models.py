from django.contrib.auth import get_user_model
from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=100)
    priority = models.PositiveIntegerField()
    display_priority = models.PositiveIntegerField()
    date_create = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)



