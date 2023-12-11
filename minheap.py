#last non leaf n/2-1
class MinHeap:
  def __init__(self, arr = []):
    self.heap = arr
    self.len = len(arr)
    self.heapify(self.len//2-1)

  def swap(self, i1: int, i2: int):
    temp = self.heap[i1]
    self.heap[i1] = self.heap[i2]
    self.heap[i2] = temp

  def heapify(self, current: int):
    if current < 0:
      return
    if current > self.len-1:
      return
    
    left = (2*current)+1
    right = (2*current)+2

    if (left > -1 and left < self.len) and (right > -1 and right < self.len):
      if self.heap[left] <= self.heap[right]:
        if self.heap[left] <= self.heap[current]:
          self.swap(current, left)
          self.siftDown(left)
          self.heapify(current-1)
      elif self.heap[right] <= self.heap[left]:
        if self.heap[right] <= self.heap[current]:
          self.swap(current, right)
          self.siftDown(right)
          self.heapify(current-1)
    elif (left > -1 and left < self.len) and (right < 0 or right > self.len-1):
      if self.heap[left] <= self.heap[current]:
        self.swap(current, left)
        self.siftDown(left)
        self.heapify(current-1)
    elif (right > -1 and right < self.len) and (left < 0 or left > self.len-1):
      if self.heap[right] <= self.heap[current]:
        self.swap(current, right)
        self.siftDown(right)
        self.heapify(current-1)
    
    return
  
  def siftDown(self, current: int):
    if current < 0:
      return
    if current > self.len-1:
      return
    
    left = (2*current)+1
    right = (2*current)+2

    if (left > -1 and left < self.len) and (right > -1 and right < self.len):
      if self.heap[left] <= self.heap[right]:
        if self.heap[left] <= self.heap[current]:
          self.swap(current, left)
          self.siftDown(left)
      elif self.heap[right] <= self.heap[left]:
        if self.heap[right] <= self.heap[current]:
          self.swap(current, right)
          self.siftDown(right)
    elif (left > -1 and left < self.len) and (right < 0 or right > self.len-1):
      if self.heap[left] <= self.heap[current]:
        self.swap(current, left)
        self.siftDown(left)
    elif (right > -1 and right < self.len) and (left < 0 or left > self.len-1):
      if self.heap[right] <= self.heap[current]:
        self.swap(current, right)
        self.siftDown(right)
    
    return
  
  def getMin(self):
    return self.heap[0]
  
  def extractMin(self):
    result = self.heap[0]
    self.heap[0] = self.heap[self.len-1]
    self.heap.pop()
    self.len -= 1
    self.siftDown(0)
    return result

  def add(self, data):
    self.heap.append(data);
    self.len += 1
    self.siftUp(self.len-1)

  def siftUp(self, current: int):
    if current < 0:
      return
    if current > self.len-1:
      return
    
    parent = (current-1)//2

    if parent < 0:
      return
    
    if self.heap[current] <= self.heap[parent]:
      self.swap(current, parent)
      self.siftUp(parent)
    
    return

  def size(self):
    return self.len