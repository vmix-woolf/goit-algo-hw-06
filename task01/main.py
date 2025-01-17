from nodes_and_edges import routes, edge_weights
from task01.graph_creation import create_graph
from task01.visualization import visualize


def main():
    G = create_graph(routes, edge_weights)
    visualize(G)


if __name__ == '__main__':
    main()
