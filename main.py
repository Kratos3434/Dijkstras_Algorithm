from minheap import MinHeap
from graph import MatrixGraph

graph = MatrixGraph(6)
graph.add_edge(0,1,4)
graph.add_edge(0,2,5)
graph.add_edge(1,3,9)
graph.add_edge(1,4,7)
graph.add_edge(1,2,11)
graph.add_edge(2,4,3)
graph.add_edge(3,5,2)
graph.add_edge(3,4,13)
graph.add_edge(4,5,6)

def dijkstra(graph):
  visited = [0]
  result = []
  heap = MinHeap(graph.get_edges(0))
  while len(visited) != graph.size():
    shortest = heap.extractMin()

    cost = shortest[0]
    fr = shortest[1]
    to = shortest[2]

    while True:
      if to not in visited:
        result.append(shortest)
        visited.append(to)
        break
      if to in visited:
        shortest = heap.extractMin()
        cost = shortest[0]
        fr = shortest[1]
        to = shortest[2]
  
    res = graph.get_edges(to)
    for i in range(len(res)):
      res[i][0] += cost
      heap.add(res[i])

  return result

print(dijkstra(graph))
# print(graph.get_edges(0))
