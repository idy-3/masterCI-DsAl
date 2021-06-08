class Stack(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) -1]

  def size(self):
    return len(self.items)


class Queue(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)


# q = Queue()

# print(q.isEmpty())
# q.enqueue(1)
# q.enqueue(2)
# print(q.dequeue())


class Deque(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    return self.items.insert(0, item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)