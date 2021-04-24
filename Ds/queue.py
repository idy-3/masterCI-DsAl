# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

# class Queue:
#   def __init__(self):
#     self.first = None
#     self.last = None
#     self.length = 0

#   def peek(self):
#     if self.first is None:
#       return None
#     return self.first.value

#   def enqueue(self, value):
#     newNode = Node(value)
#     if self.length == 0:
#       self.first = newNode
#       self.last = newNode
#     else:
#       self.last.next = newNode
#       self.last = newNode
#     self.length+=1


#   def dequeue(self):
#     if self.first is None:
#       return None
#     if self.first == self.last:
#       self.last = None
#     temp = self.first
#     self.first = temp.next
#     temp.next = None
#     self.length-=1
#     return temp.value

#   def isEmpty(self):
#     if self.first is None:
#       return True
#     return False

#   def printList(self):
#     curNode = self.first
#     while curNode is not None:
#       print(curNode.value, end="-->")
#       curNode = curNode.next
#     print()

# myQueue = Queue()
# myQueue.enqueue("joy")
# myQueue.enqueue("matt")
# myQueue.enqueue("pavel")
# print(myQueue.peek())
# myQueue.enqueue("samir")
# myQueue.printList()
# myQueue.dequeue()
# myQueue.dequeue()
# myQueue.dequeue()
# myQueue.printList()

# # --------------
# Queues using stacks

class QueueStacks:
  def __init__(self):
    self.first = []
    self.last = []

  def enqueue(self, value):
    self.first.append(value)
    return self

  def dequeue(self):
    if len(self.last) == 0 and len(self.first) == 0:
      return "empty"
    elif len(self.last) == 0 and len(self.first) > 0:
      for i in range(len(self.first)):
        self.last.append(self.first.pop())
      return self.last.pop()
    else:
      return self.last.pop()

  def peek(self):
    if(len(self.last) > 0):
      return self.last[0]

    return self.first[len(self.first) -1]


myQueue =  QueueStacks()
# myQueue.peek()
print(myQueue.enqueue('Joy').__dict__)
print(myQueue.enqueue('Matt').__dict__)
print(myQueue.dequeue())
print(myQueue.enqueue('Pavel').__dict__)
myQueue.peek()
print(myQueue.dequeue())
print(myQueue.dequeue())
# print(myQueue.peek())
