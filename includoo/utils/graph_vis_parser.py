#!usr/bin/pthon3

class GraphVisParser():
    """
    args:
        graph_data: a list of data points containing 
                    the node and edge info, in the form of
                    [(id1),  ...                            // nodes
                    (id1, id2, {'weight': weight12}), ...]  //edges

    return:
        vis_graph_data: a list of parsed data points
                        ready to be used for the graph visualisation
    """
    def __init__(self, graph_data):
        self.graph_data = graph_data

    def run():
        vis_graph_data = []
        id_count = 0
        for row in self.graph_data:
            if len(row) == 1:
                vis_graph_data.append({data: {id: id_count}})
            else:
                try:
                    vis_graph_data.append({data: {id: id_count,
                                                    source: row[0],
                                                    target: row[1],
                                                    weight: row[2]['weight']}})
        return vis_graph_data


if __init__ == "__main__":
    graphVisParser = GraphVisParser(graph_data)
    graphVisParser.run()