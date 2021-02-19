def buildgraph(edges):
  graph = {}
  for parent, child in edges:
    if parent not in graph:
      graph[parent] = set()
    if child not in graph:
      graph[child] = set()
    
    graph[child].add(parent)
  
  return graph
def zeroOrOneParent(edges):
  res = []
  if edges == None or len(edges) == 0:
    return res

  graph = buildgraph(edges)
  
  for k in graph.keys():
    if len(graph[k]) <= 1:
      res.append(k)
  
  return res
edges = [[1,4], [1,5], [2,5], [3,6],[6,7]]
#print(zeroOrOneParent(edges))

def zeroOrOneParent(edges):
  res = []
  if edges == None or len(edges) == 0:
    return res
  graph = buildgraph(edges)

def helper(visited, graph, node):
    if node not in visited:
      print(node)
      visited.add(node)
      for neighbor in graph[node]:
        helper(visited,graph, neighbor)
def dfs(edges):
  res = []
  if edges == None or len(edges) == 0:
    return res
  graph = buildgraph(edges)
  visited = set()
  
  helper(visited,graph, 7)
  return visited


