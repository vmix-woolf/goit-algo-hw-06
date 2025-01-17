import networkx as nx


def create_graph(routes, edge_weights)-> nx.Graph:
    G = nx.Graph()
    sorted_edge_weights = {tuple(sorted(edge)): weight for edge, weight in edge_weights.items()}
    # add routes to the graph
    for route, stops in routes.items():
        for i in range(len(stops) - 1):
            stop1 = stops[i]
            stop2 = stops[i + 1]
            edge = tuple(sorted([stop1, stop2]))
            travel_time = sorted_edge_weights.get(edge)
            if travel_time is None:
                raise ValueError(f"weight for edge {edge} is not found in sorted_edge_weights")
            G.add_edge(stop1, stop2, weight=travel_time, color=route)
    return G