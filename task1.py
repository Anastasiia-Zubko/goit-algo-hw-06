"""
City Transportation Network Analysis
"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Task 1: Create and Visualize a Graph Model
def create_graph():
    """
    Create a graph representing a city's transportation network.
    """
    G = nx.Graph() 
    locations = ["Home", "Work", "Gas Station", "Mall", "Hospital", "Library", "Cafe", "Gym"]
    edges = [
        ("Home", "Work"), ("Home", "Gas Station"), ("Work", "Mall"),
        ("Mall", "Hospital"), ("Hospital", "Library"), ("Library", "Cafe"),
        ("Cafe", "Gym"), ("Gym", "Home"), ("Gas Station", "Mall"), ("Mall", "Cafe"),
        ("Cafe", "Home"), ("Gas Station", "Hospital")
    ]
    G.add_nodes_from(locations)
    G.add_edges_from(edges)
    return G

def visualize_graph(G, pos=None):
    """
    Visualize the graph using Matplotlib.
    """
    plt.figure(figsize=(12, 8))
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=10000,
            edge_color="gray", font_size=15, font_weight="bold")

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("City Transportation Network")
    plt.show()

def analyze_graph(G):
    """
    Analyze and print the main characteristics of the graph.
    """
    print(f"Number of vertices (nodes): {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Degrees of vertices: {dict(G.degree())}")

# Task 2: Implement DFS and BFS Algorithms
def convert_to_dict(G):
    """
    Convert the NetworkX graph to a dictionary for DFS and BFS.
    """
    return {node: list(G[node]) for node in G}

def dfs_iterative(graph, start_vertex):
    """
    Perform iterative Depth-First Search (DFS) on the graph.
    """
    visited = set()
    stack = [start_vertex]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            path.append(vertex)
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    return path

def bfs_iterative(graph, start):
    """
    Perform iterative Breadth-First Search (BFS) on the graph.
    """
    visited = set()
    queue = deque([start])
    path = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            path.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return path

# Task 3: Implement Dijkstra's Algorithm
def dijkstra(graph, start):
    """
    Implement Dijkstra's algorithm to find the shortest path in the graph.
    """
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get('weight', 1)
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

def main():
    """
    Main function to run the tasks.
    """
    # Task 1
    G = create_graph()
    visualize_graph(G)
    analyze_graph(G)

    # Convert the NetworkX graph to a dictionary for DFS and BFS
    graph_dict = convert_to_dict(G)

    # Task 2
    start_node = "Home"
    goal_node = "Cafe"
    dfs_path = dfs_iterative(graph_dict, start_node)
    bfs_path = bfs_iterative(graph_dict, start_node)
    print(f"DFS path from {start_node} to {goal_node}: {dfs_path}")
    print(f"BFS path from {start_node} to {goal_node}: {bfs_path}")

    # Task 3
    weighted_edges = [
        ("Home", "Work", 1), ("Home", "Gas Station", 2), ("Work", "Mall", 2),
        ("Mall", "Hospital", 3), ("Hospital", "Library", 2), ("Library", "Cafe", 1),
        ("Cafe", "Gym", 3), ("Gym", "Home", 2), ("Gas Station", "Mall", 1), ("Mall", "Cafe", 1),
        ("Cafe", "Home", 4), ("Gas Station", "Hospital", 2)
    ]
    G.clear()
    G.add_weighted_edges_from(weighted_edges)
    visualize_graph(G)
    distances = dijkstra(G, start_node)
    print(f"Shortest distances from {start_node}: {distances}")

if __name__ == "__main__":
    main()
