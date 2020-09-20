from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Edge

from .serializers import EdgeSerializer


class EdgeAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        edges = Edge.objects.all()
        serializer = EdgeSerializer(edges, many=True)
        return Response(serializer.data)
