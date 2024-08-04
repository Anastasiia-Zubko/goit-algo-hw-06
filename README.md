## Task 1: Create and Visualize a Graph Model

A city's transportation network was modeled using NetworkX. The graph was visualized and its main characteristics were analyzed.

- **Graph Analysis:**
  - **Number of vertices (nodes):** 8
  - **Number of edges:** 12
  - **Degrees of vertices:** 
    - Home: 4
    - Work: 2
    - Gas Station: 3
    - Mall: 4
    - Hospital: 3
    - Library: 2
    - Cafe: 4
    - Gym: 2

## Task 2: Implement DFS and BFS Algorithms

DFS and BFS algorithms were implemented to find paths in the graph. The paths obtained by each algorithm were compared.

- **DFS Path from Home to Cafe:** 
  - Home, Work, Mall, Hospital, Library, Cafe, Gym, Gas Station
- **BFS Path from Home to Cafe:** 
  - Home, Gym, Work, Gas Station, Cafe, Mall, Hospital, Library

DFS goes deep into one branch before trying another, while BFS checks all neighbors at the current level before moving deeper. This explains the different paths they take.

## Task 3: Implement Dijkstra's Algorithm

Dijkstra's algorithm was implemented to find the shortest path between all graph vertices. Weights were added to the edges of the graph.

- **Shortest Distances from Home:**
  - Home: 0
  - Work: 1
  - Gas Station: 2
  - Mall: 3
  - Hospital: 4
  - Library: 5
  - Cafe: 4
  - Gym: 2
