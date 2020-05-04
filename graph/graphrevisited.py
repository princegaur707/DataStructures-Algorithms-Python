from collections import deque

graph = { "Alice":  ["Bob", "Claire", "Frank"],
      "Bob":    ["Alice"],
      "Claire": ["Alice", "Dennis", "Esther", "Frank"],
      "Dennis": ["Claire", "Esther", "George"],
      "Esther": ["Claire", "Dennis"],
      "Frank":  ["Alice", "Claire", "George"],
      "George": ["Dennis", "Frank"]
    }
# T.C O(V.E)
def getEdges(graph):
    edges=[]
    
    for vertex in graph:
        for neighbour in graph[vertex]:
            edges.append((vertex,neighbour))
    
    return edges

# dfs -> stack / recursion T.C O(V+E)
def dfs(graph,start,visited=[]):
    visited.append(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    
    return visited

 # bfs -> queue / iteration T.C O(V+E)
def bfs(graph,start,visited=[]):
    queue = deque()
    visited.append(start)
    queue.append(start)
    
    while queue:
        s = queue.popleft()
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
    return visited

def findAllPaths(graph,start,end,path=[]):
    
    if start not in graph:
        return []
    
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    
    for neighbour in graph[start]:
        if neighbour not in path:
            newpaths = findAllPaths(graph,neighbour,end,path)
            for newpath in newpaths:
                paths.append(newpath)
                
    return paths

def findShortestPath(graph,start,end,visited=[]):
    dist = {start : [start]}
    queue = deque()
    queue.append(start)
    while queue:
        s = queue.popleft()
        for neighbour in graph[s]:
            if neighbour not in dist:
                dist[neighbour] = dist[s] + [neighbour]
                queue.append(neighbour)
    return dist[end]
                

print(dfs(graph,'Alice'))
print(bfs(graph,'Alice'))
print(findAllPaths(graph,'Alice','Dennis'))
print(findShortestPath(graph,'Alice','Dennis'))
print(findAllPaths(graph,'Alice','George'))
print(findShortestPath(graph,'Alice','George'))
    
    

