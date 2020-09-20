from django.db import models
from includoo.users.models import User


class Edge(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="user1", blank=True, null=True, default=0)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="user2", blank=True, null=True, default=0)
    weight = models.FloatField()
