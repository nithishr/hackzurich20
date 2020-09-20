from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Edge
from includoo.users.models import User

from .serializers import EdgeSerializer


class EdgeAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        edges = Edge.objects.all()
        serializer = EdgeSerializer(edges, many=True)
        return Response(serializer.data)

    def post(self, request):
        sender = request.data["sender"]
        recipient = request.data["recipient"]
        mails = request.data["mails"]

        s_user = User.objects.filter(email=sender)
        r_user = User.objects.filter(email=recipient)

        weight = sum(mails)
        e = Edge.objects.filter(user1=s_user[0], user2=r_user[0])
        if e:
            e.update(user1=s_user[0], user2=r_user[0], weight=weight)
        else:
            e = Edge.objects.filter(user2=s_user[0], user1=r_user[0])
            if not e:
                e.create(user1=s_user[0], user2=r_user[0], weight=weight)
            else:
                e.update(user2=s_user[0], user1=r_user[0], weight=weight)


        return Response()



