from queue import Queue
import networkx as nx

square_graph_nodes = [1, 2, 3, 4]
square_graph_edges = [(1, 2, {"weight": 1}), (2, 3, {"weight": 0.4}),
                (1, 3, {"weight": 0.4}), (3, 4, {"weight": 0.1})]
square_graph_interests = {1: [1, 0, 1, 1], 2: [0, 0, 0, 0], 3: [0, 0, 1, 0],
                          4: [1, 1, 1, 1]}
meeting_scores = [(0, 0.5), (1, 0.85), (2, 1)]
meeting_interests = {1: [1, 0, 0], 2: [0, 1, 0], 3: [1, 0, 1], 4: [1, 1, 1]}

FLOW_DECAY = 0.5

def dump_flows(G):
    print("*******")
    for node in G.nodes:
        print("Node {} has flow {}".format(node, G.nodes[node]["flow"]))

def compute_flow(G):
    for node in G.nodes:
        for n2 in G.nodes:
            G.nodes[n2]["flow_buffer"] = 0
        visited = set()
        bfs_queue = Queue()
        bfs_queue.put(node)
        G.nodes[node]["flow_buffer"] += 1
        G.nodes[node]["flow"] += 1
        while not len(visited) == len(G.nodes):
            cur_node = bfs_queue.get()
            if cur_node in visited:
                continue
            for adj in G[cur_node]:
                if adj not in visited:
                    new_flow = G.nodes[cur_node]["flow_buffer"] * G[cur_node][adj]["weight"] \
                            * FLOW_DECAY
                    G.nodes[adj]["flow"] += new_flow
                    G.nodes[adj]["flow_buffer"] += new_flow
                    bfs_queue.put(adj)
            visited.add(cur_node)
    max_flow = 0
    for node in G.nodes:
        max_flow = max(max_flow, G.nodes[node]["flow"])
    for node in G.nodes:
        G.nodes[node]["flow"] /= max_flow

def compute_interest_score(interestsA, interestsB):
    return sum([a*b for a,b in zip(interestsA, interestsB)]) / len(interestsA)

def compute_final_score(flow, interest_score):
    return 1.25 * flow + interest_score

def have_shared_meeting_interests(meeting_interestsA, meeting_interestsB):
    return sum([a*b for a,b in zip(meeting_interestsA, meeting_interestsB)]) > 0

def get_meeting(meeting_interestsA, meeting_interestsB):
    meetings_sorted = sorted(meeting_scores, key=lambda x: x[1], reverse=True)
    for meeting in meetings_sorted:
        index = meeting[0]
        if meeting_interestsA[index] == 1 and meeting_interestsB[index] == 1:
            return index
    return None

def match(G):
    compute_flow(G)
    #dump_flows(G)
    nodes_flow = sorted(G.nodes, key=lambda x: G.nodes[x]["flow"])
    total_matches = []
    matched = set()
    for nodeA in nodes_flow:
        if nodeA in matched:
            continue
        interest_scores = dict()
        interestsA = square_graph_interests[nodeA]
        for nodeB in G.nodes:
            interestsB = square_graph_interests[nodeB]
            interest_scores[nodeB] = compute_interest_score(interestsA, interestsB)
        matches = [(compute_final_score(G.nodes[other]["flow"], interest_scores[other]), other) for other in G.nodes]
        matches = sorted(matches, key=lambda x: x[0], reverse=True)
        matches = list(filter(lambda x: have_shared_meeting_interests(meeting_interests[x[1]], meeting_interests[nodeA]) and x[1] != nodeA, matches))
        for cur_match in matches:
            nodeA_match = cur_match
            matching_node = nodeA_match[1]
            if not matching_node in matched:
                meeting = get_meeting(meeting_interests[nodeA], meeting_interests[matching_node])
                total_matches.append((nodeA, matching_node, meeting))
                matched.add(nodeA)
                matched.add(matching_node)
                break
    return total_matches

def list_to_nx(nodes_list, edges_list):
    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(nodes_list)
    for node in nx_graph.nodes:
        nx_graph.nodes[node]["flow"] = 0
    nx_graph.add_edges_from(edges_list)
    nx_graph = nx_graph.to_undirected()
    return nx_graph

G = list_to_nx(square_graph_nodes, square_graph_edges)
print(match(G))
