from django.urls import path

from includoo.graph.views import (
    index
)

app_name = "graph"
urlpatterns = [
    path("get_connections/", view=index),
]
