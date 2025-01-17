from task02.bfs import bfs
from task02.dfs import dfs
from task01.graph_creation import create_graph
from task01.nodes_and_edges import routes, edge_weights


def main():
    start_node = 'T'
    end_node = 'I'

    G = create_graph(routes, edge_weights)

    dfs_path = dfs(G, start_node, end_node)
    bfs_path = bfs(G, start_node, end_node)

    print("DFS path:", " -> ".join(dfs_path) if dfs_path else "Route is not found")
    print("BFS path:", " -> ".join(bfs_path) if bfs_path else "Route is not found")


if __name__ == '__main__':
    main()