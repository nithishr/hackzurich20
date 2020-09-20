from django.contrib.auth import get_user_model
from .video_together import create_room

User = get_user_model()


def edge_set_to_edge_list(edge_set):
    edge_list = []
    for edge in edge_set:
        new_edge = (edge.user1.id, edge.user2.id, {"weight": edge.weight})
        edge_list.append(new_edge)
    return edge_list

def user_set_to_node_list(user_set):
    node_list = []
    for user in user_set:
        node_list.append(user.id)
    return node_list

def user_set_to_topic_interests(user_set):
    interests = dict()
    b_to_i = lambda b: 1 if b else 0 # boolean to int
    for user in user_set:
        interests[user.id] = [b_to_i(user.interest_sports),
                              b_to_i(user.interest_arts),
                              b_to_i(user.interest_social),
                              b_to_i(user.interest_env),
                              b_to_i(user.interest_drinks),
                              b_to_i(user.interest_startups),
                              b_to_i(user.interest_games),
                              b_to_i(user.interest_photography)]
    return interests

def user_set_to_meeting_interests(user_set):
    interests = dict()
    for user in user_set:
        interests[user.id] = [1, 1, 1]
    return interests

def id_to_user(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        print("PANIC")
    return None

def match_to_meeting(matches):
    meetings = []
    for match in matches:
        meeting = (id_to_user(match[0]).email,
                   id_to_user(match[1]).email,
                   create_room())
        meetings.append(meeting)
    return meetings
