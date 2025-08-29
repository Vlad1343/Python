
# # Define the decision tree as a dictionary
# tree = {
#     'A': ['B', 'C'],  # Node A connects to B and C
#     'B': ['D', 'E'],  # Node B connects to D and E
#     'C': ['F', 'G'],  # Node C connects to F and G
#     'D': ['H', 'I'],  # Node D connects to H and I
#     'E': ['J', 'K'],  # Node E connects to J and K
#     'F': ['L', 'M'],  # Node F connects to L and M
#     'G': ['N', 'O'],  # Node G connects to N and O
#     'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
#     'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
# }

# from collections import deque  # Import deque for efficient queue operations

# # Define the BFS function
# def bfs(tree, start):
#     visited = []  # List to keep track of visited nodes
#     queue = deque([start])  # Initialize the queue with the starting node

#     while queue:  # While there are still nodes to process
#         node = queue.popleft()  # Dequeue a node from the front of the queue

#         if node not in visited:  # Check if the node has been visited
#             visited.append(node)  # Mark the node as visited
#             print(node, end=" ")  # Output the visited node

#             # Enqueue all unvisited neighbors (children) of the current node
#             for neighbor in tree[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)  # Add unvisited neighbors to the queue
            
            
# bfs(tree, 'A')







# # Function to find BFS of Graph from given source s
# def bfs(adj):
    
#     # get number of vertices
#     V = len(adj)
    
#     # create an array to store the traversal
#     res = []
#     s = 0
#     # Create a queue for BFS
#     from collections import deque
#     q = deque()
    
#     # Initially mark all the vertices as not visited
#     visited = [False] * V
    
#     # Mark source node as visited and enqueue it
#     visited[s] = True
#     q.append(s)
    
#     # Iterate over the queue
#     while q:
        
#         # Dequeue a vertex from queue and store it
#         curr = q.popleft()
#         res.append(curr)
        
#         # Get all adjacent vertices of the dequeued 
#         # vertex curr If an adjacent has not been 
#         # visited, mark it visited and enqueue it
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x] = True
#                 q.append(x)
                
#     return res

# if __name__ == "__main__":
    
#     # create the adjacency list
#     # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
#     adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
#     ans = bfs(adj)
#     for i in ans:
#         print(i, end=" ")






# """BFS Traversal of a Graph"""
# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# visited = [] # List to keep track of visited nodes
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s, end = " ") 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')



# """BFS Traversal of a Graph"""
# import collections
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C', 'E'],
#     'E': ['D'],
# }
# def bfs(g, root):
#     queue = collections.deque(root)
#     visited = []
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#         for item in g[node]:         #g is a dictionary, node is a key(keys)
#             if item not in visited:
#                 queue.append(item)   
#     print(visited)
# bfs(graph, 'A')






graph = { 
'0' : ['3' , '5', '9' ],
'1': ['6', '7', '4'],
'2': ['10', '5'],
'3': ['0'],
'4': ['1', '5', '8'],
'5': ['2', '0', '4'],
'6': ['1'],
'7': ['1'],
'8': ['4'],
'9': ['0'],
'10': ['2']
}
"""Find all nodes in a graph using BFS"""
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    return visited
print(bfs(graph, '0'))

"""Find the shortest path in a graph using BFS"""
def bfsShortest(graph, start, end):
    visited = []
    queue = [start]
    parent = {}
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = current_node
                
    print(shortPath(parent, start, end))
def shortPath(parent, start, end):
    path = [end]
    current_node = end
    while current_node != start:
        current_node = parent[current_node]
        path.append(current_node)
    path.reverse()
    return path
bfsShortest(graph, '0', '10')




# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []

# from collections import deque

# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person + " is a mango seller!")
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False

# def person_is_seller(name):
#     return name[-1] == "m"

# if __name__ == "__main__":
#     if search("you"):
#         print("Mango seller found!")
#     else:
#         print("No mango seller found.")