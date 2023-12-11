class MatrixGraph:
  def __init__(self, size):
    self.len = size
    self.graph = []
    for i in range(size):
      self.graph.append([0 for i in range(size)])
    self.numEdge = 0

  def size(self):
    return self.len

  def add_edge(self, i1, i2, weight=1):
    self.graph[i1][i2] = weight
    self.graph[i2][i1] = weight
    self.numEdge += 1

  def has_edge(self, i1, i2):
    return self.graph[i1][i2] != 0

  def get_edges(self, i1):
    res = []
    for i in range(self.len-1):
      if self.has_edge(i1, i+1):
        res.append([self.graph[i1][i+1], i1, i+1])
    return res

  def size(self):
    return self.len