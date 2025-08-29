## Decision Tree Traversal using DFS
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H', 'I'],
#     'E': ['J', 'K'],
#     'F': ['L', 'M'],
#     'G': ['N', 'O'],
#     'H': [], 'I': [], 'J': [], 'K': [],
#     'L': [], 'M': [], 'N': [], 'O': []

# }
# # Recursive DFS function
# def dfs_recursive(tree, node, visited=None):
#     if visited is None:
#         visited = set()  # Initialize the visited set
#     visited.add(node)    # Mark the node as visited
#     print(node)          # Print the current node (for illustration)
#     for child in tree[node]:  # Recursively visit children
#         if child not in visited:
#             dfs_recursive(tree, child, visited)

# # Run DFS starting from node 'A'
# dfs_recursive(tree, 'A')


# # Iterative DFS function
# def dfs_iterative(tree, start):
#     visited = set()  # Track visited nodes
#     stack = [start]  # Stack for DFS

#     while stack:  # Continue until stack is empty
#         node = stack.pop()  # Pop a node from the stack
#         if node not in visited:
#             visited.add(node)  # Mark node as visited
#             print(node)        # Print the current node (for illustration)
#             stack.extend(reversed(tree[node]))  # Add child nodes to stack

# # Run DFS starting from node 'A'
# dfs_iterative(tree, 'A')




## Adjacency Matrix DFS
# def dfsRec(adj, visited, s, res):
#     visited[s] = True
#     res.append(s)

#     # Recursively visit all adjacent vertices that are not visited yet
#     for i in range(len(adj)):
#         if adj[s][i] == 1 and not visited[i]:
#             dfsRec(adj, visited, i, res)

# def dfs(adj):
#     visited = [False] * len(adj)
#     res = []
#     dfsRec(adj, visited, 0, res)  # Start DFS from vertex 0
#     return res

# def add_edge(adj, s, t):
#     adj[s][t] = 1
#     adj[t][s] = 1  # Since it's an undirected graph

# # Driver code
# V = 5
# adj = [[0] * V for _ in range(V)]  # Adjacency matrix

# # Define the edges of the graph
# edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

# # Populate the adjacency matrix with edges
# for s, t in edges:
#     add_edge(adj, s, t)

# res = dfs(adj)  # Perform DFS
# print(" ".join(map(str, res)))





## Adjacency List using defaultdict(list)
# # Create an adjacency list for the graph
# from collections import defaultdict

# def add_edge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)

# # Recursive function for DFS traversal

# def dfs_rec(adj, visited, s, res):
#     # Mark the current vertex as visited
#     visited[s] = True
#     res.append(s)

#     # Recursively visit all adjacent vertices that are not visited yet
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj, visited, i, res)

# # Main DFS function to perform DFS for the entire graph

# def dfs(adj):
#     visited = [False] * len(adj)
#     res = []
#     # Loop through all vertices to handle disconnected graph
#     for i in range(len(adj)):
#         if not visited[i]:
#             # If vertex i has not been visited,
#             # perform DFS from it
#             dfs_rec(adj, visited, i, res)
#     return res

# V = 6
# # Create an adjacency list for the graph
# adj = defaultdict(list)

# # Define the edges of the graph
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]

# # Populate the adjacency list with edges
# for e in edges:
#     add_edge(adj, e[0], e[1])
# res = dfs(adj)

# print(' '.join(map(str, res)))






## DFS traversal of a graph using adjacency list
# graph = {
#     'A': ['B', 'C', 'D'],
#     'B': ['E'],
#     'C': ['G', 'F'],
#     'D': ['H'],
#     'E': ['I'],
#     'F': ['J'],
#     'G': ['K'],
#     'H': [],
#     'I': [],
#     'J': [],
#     'K': []
# }
# #Recursive DFS function
# def dfs_recursive(graph, node, visited):
#     if node not in visited:
#         print(node, end=' ')
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs_recursive(graph, neighbour, visited)

# visited = set()
# print("DFS traversal using recursive approach:")
# dfs_recursive(graph, 'A', visited)

## Iterative DFS function
# def dfs_iterative(graph, start):
#     visited = set()
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
# print("\nDFS traversal using iterative approach:")
# dfs_iterative(graph, 'A')







## Fastest Path Finder (DFS for all paths)
network = {
    'Computer1': ['Computer2', 'Computer3'],
    'Computer2': ['Computer4'],
    'Computer3': ['Computer4', 'Computer5'],
    'Computer4': ['Computer6'],
    'Computer5': ['Computer6'],
    'Computer6': []
}
def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

start = 'Computer1'
end = 'Computer6'
print(f"All paths from {start} to {end}:")
paths = find_paths(network, start, end)
for path in paths:
    print(" -> ".join(path))
    
    


# class Solution:
#     def dfs(self, V, adj):
#         visited = [False] * V
#         result = []

#         def dfs_util(node):
#             visited[node] = True
#             result.append(node)
#             for neighbor in adj[node]:  # traverse neighbors in given order
#                 if not visited[neighbor]:
#                     dfs_util(neighbor)

#         dfs_util(0)  # start from node 0
#         return result

# if __name__ == "__main__":
#     V = 5
#     adj = [[2, 3, 1], [0], [0, 4], [0], [2]] 
#     solution = Solution()
#     result = solution.dfs(V, adj)
#     print(result)






## Different DFS Traversals of a Tree



##Inorder traversal

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# # A function to do inorder tree traversal
# def printInorder(root):

#     if root:

#         # First recur on left child
#         printInorder(root.left)

#         # then print the data of node
#         print(root.val),

#         # now recur on right child
#         printInorder(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)

# printInorder(root)





##Preorder Traversal

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# # A function to do preorder tree traversal


# def printPreorder(root):

#     if root:

#         # First print the data of node
#         print(root.val),

#         # Then recur on left child
#         printPreorder(root.left)

#         # Finally recur on right child
#         printPreorder(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right = Node(6)
# printPreorder(root)




##Postorder Traversal

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# # A function to do postorder tree traversal
# def printPostorder(root):

#     if root:

#         # First recur on left child
#         printPostorder(root.left)

#         # the recur on right child
#         printPostorder(root.right)

#         # now print the data of node
#         print(root.val),


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)

# printPostorder(root)