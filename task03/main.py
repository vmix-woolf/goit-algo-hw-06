import networkx as nx
from task01.graph_creation import create_graph
from task01.nodes_and_edges import routes, edge_weights
from task03.dijkstra import dijkstra

def main():
    G = create_graph(routes, edge_weights)

    shortest_paths = nx.single_source_dijkstra_path(G, source='A')
    shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='A')

    print(shortest_path_lengths)  #

    print("\nвиведе найкоротші шляхи від вузла 'A' до всіх інших вузлів")
    for key, value in shortest_paths.items():
        print(f"{key}: {value}")

    print("\nвиведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів")
    for key, value in shortest_path_lengths.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()