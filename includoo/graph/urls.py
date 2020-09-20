from django.urls import path

from includoo.graph.views import (
    EdgeAPI
)

app_name = "graph"
urlpatterns = [
    path("list_edges/", view=EdgeAPI.as_view()),
]
