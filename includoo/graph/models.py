from django.db import models
from includoo.users.models import User
from includoo.organizations.models import Organization


class Node(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Edge(models.Model):
    node1 = models.ForeignKey(Node, on_delete=models.CASCADE,
                              related_name="node1")
    node2 = models.ForeignKey(Node, on_delete=models.CASCADE,
                              related_name="node2")
    weight = models.FloatField()
