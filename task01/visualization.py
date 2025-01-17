import networkx as nx
import matplotlib.pyplot as plt

def visualize(graph: nx.Graph):
    # visualization
    pos = nx.spring_layout(graph)
    edges = graph.edges()
    weights = [graph[u][v]['weight'] for u, v in edges]
    colors = [graph[u][v]['color'] for u, v in edges]

    plt.figure(figsize=(12, 10))
    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=500,
        node_color='lightblue'
    )
    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=11,
        font_color='black',
    )
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=edges,
        width=3,
        edge_color=colors,
        alpha=0.8
    )

    edge_labels = {(u, v): f"{graph[u][v]['weight']}" for u, v in edges}
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels,
        font_size=8,
        font_color='darkblue'
    )

    plt.title("Транспортна мережа тролейбусів міста Одеси", fontsize=14)
    plt.axis('on')
    plt.show()