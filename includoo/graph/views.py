from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Edge
from includoo.users.models import User

from .serializers import EdgeSerializer
from .tasks import edge_set_to_edge_list, user_set_to_node_list
from .tasks import user_set_to_topic_interests, user_set_to_meeting_interests
from .tasks import match_to_meeting
from .algorithm import compute_match

User = get_user_model()

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

        meeting_suggestions = get_meeting_suggestions()
        return Response(meeting_suggestions)


def get_meeting_suggestions():
    nodes = User.objects.all()
    node_list = user_set_to_node_list(nodes)
    print(node_list)
    edges = Edge.objects.all()
    edge_list = edge_set_to_edge_list(edges)
    topic_interests = user_set_to_topic_interests(nodes)
    print(topic_interests)
    meeting_interests = user_set_to_meeting_interests(nodes)
    print(meeting_interests)
    #serializer = EdgeSerializer(edges, many=True)
    matches = compute_match(node_list, edge_list, topic_interests,
                            meeting_interests)
    result = match_to_meeting(matches)
    return result

class MatchAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        suggestions = get_meeting_suggestions()
        return Response(suggestions)
        #return Response(serializer.data)
