## Dijkstra's Algorithm for finding the shortest path in a graph

# class Graph():

#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                       for row in range(vertices)]

#     def printSolution(self, dist):
#         print("Vertex \t Distance from Source")
#         for node in range(self.V):
#             print(node, "\t\t", dist[node])

#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minDistance(self, dist, sptSet):

#         # Initialize minimum distance for next node
#         min = 1e7

#         # Search not nearest vertex not in the
#         # shortest path tree
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v

#         return min_index

#     # Function that implements Dijkstra's single source
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):

#         dist = [1e7] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V

#         for cout in range(self.V):

#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # u is always equal to src in first iteration
#             u = self.minDistance(dist, sptSet)

#             # Put the minimum distance vertex in the
#             # shortest path tree
#             sptSet[u] = True

#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             for v in range(self.V):
#                 if (self.graph[u][v] > 0 and 
#                    sptSet[v] == False and 
#                    dist[v] > dist[u] + self.graph[u][v]):
#                     dist[v] = dist[u] + self.graph[u][v]

#         self.printSolution(dist)

# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]

# g.dijkstra(0)







## Dijkstra's Algorithm Implementation in Python

# import heapq
# import sys

# # Function to construct adjacency 
# def constructAdj(edges, V):
    
#     # adj[u] = list of [v, wt]
#     adj = [[] for _ in range(V)]

#     for edge in edges:
#         u, v, wt = edge
#         adj[u].append([v, wt])
#         adj[v].append([u, wt])

#     return adj

# # Returns shortest distances from src to all other vertices
# def dijkstra(V, edges, src):
#     # Create adjacency list
#     adj = constructAdj(edges, V)

#     # Create a priority queue to store vertices that
#     # are being preprocessed.
#     pq = []
    
#     # Create a list for distances and initialize all
#     # distances as infinite
#     dist = [sys.maxsize] * V

#     # Insert source itself in priority queue and initialize
#     # its distance as 0.
#     heapq.heappush(pq, [0, src])
#     dist[src] = 0

#     # Looping till priority queue becomes empty (or all
#     # distances are not finalized) 
#     while pq:
#         # The first vertex in pair is the minimum distance
#         # vertex, extract it from priority queue.
#         u = heapq.heappop(pq)[1]

#         # Get all adjacent of u.
#         for x in adj[u]:
#             # Get vertex label and weight of current
#             # adjacent of u.
#             v, weight = x[0], x[1]

#             # If there is shorter path to v through u.
#             if dist[v] > dist[u] + weight:
#                 # Updating distance of v
#                 dist[v] = dist[u] + weight
#                 heapq.heappush(pq, [dist[v], v])

#     # Return the shortest distance array
#     return dist

# # Driver program to test methods of graph class
# if __name__ == "__main__":
#     V = 5
#     src = 0

#     # edge list format: {u, v, weight}
#     edges =[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]];

#     result = dijkstra(V, edges, src)

#     # Print shortest distances in one line
#     print(' '.join(map(str, result)))




# graph = {
#     "start": {"a": 6, "b": 2},
#     "a": {"fin": 1},
#     "b": {"a": 3, "fin": 5},
#     "fin": {}
# }

# infinity = float("inf")
# costs = {
#     "a": 6,
#     "b": 2,
#     "fin": infinity
# }

# parents = {
#     "a": "start",
#     "b": "start",
#     "fin": None
# }

# processed = []

# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors:
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)

# print("Cost to each node:", costs)
# print("Parents:", parents)


