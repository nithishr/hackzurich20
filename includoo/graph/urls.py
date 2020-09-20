from django.urls import path

from includoo.graph.views import (
    EdgeAPI,
    MatchAPI
)

app_name = "graph"
urlpatterns = [
    path("list_edges/", view=EdgeAPI.as_view()),
    path("match/", view=MatchAPI.as_view()),
]
