class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def append(self, value):
    newNode = Node(value)
    self.tail.next = newNode
    self.tail = newNode
    self.length+=1

  def prepend(self, value):
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode
    self.length+=1

  def insert(self, index, value):
    if index <= 0:
      self.prepend(value)
      return self.printList()

    if index >= self.length:
      self.append(value)
      return self.printList()

    newNode = Node(value)
    curNode = self.__traverseToIndex(index-1)
    newNode.next = curNode.next
    curNode.next = newNode
    self.length+=1

  def remove(self, index):
    if index < 0:
      return "error index too small"

    if index > self.length:
      return "error index too large"

    curNode = self.__traverseToIndex(index-1)
    nodeToRemove = curNode.next
    curNode.next = curNode.next.next
    nodeToRemove.next = None
    self.length-=1
    return nodeToRemove.value

  def reverse(self):
    if self.head.next is None:
      return self.head

    first = self.head
    self.tail = self.head
    second = first.next
    while second is not None:
      temp = second.next
      second.next = first
      first = second
      second = temp
    self.head.next = None
    self.head = first

  def __traverseToIndex(self, index):
    curNode = self.head
    i = 0
    while i!=index:
      curNode = curNode.next
      i+=1
    return curNode

  def printList(self):
    curNode = self.head
    while curNode is not None:
      print(curNode.value, end="-->")
      curNode = curNode.next
    print()
    


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2,99)
myLinkedList.printList()
myLinkedList.remove(2)
myLinkedList.printList()
myLinkedList.reverse()
myLinkedList.printList()


# # -------------------------

# class DLLNode:
#   def __init__(self, value):
#     self.value = value
#     self.next = None
#     self.prev = None

# class DoublyLinkedList:
#   def __init__(self, value):
#     self.head = DLLNode(value)
#     self.tail = self.head
#     self.length = 1

#   def append(self, value):
#     newNode = DLLNode(value)
#     newNode.prev = self.tail
#     self.tail.next = newNode
#     self.tail = newNode
#     self.length+=1

#   def prepend(self, value):
#     newNode = DLLNode(value)
#     newNode.next = self.head
#     self.head.prev = newNode
#     self.head = newNode
#     self.length+=1

#   def insert(self, index, value):
#     if index <= 0:
#       self.prepend(value)
#       return self.printList()

#     if index >= self.length:
#       self.append(value)
#       return self.printList()

#     newNode = DLLNode(value)
#     curNode = self.__traverseToIndex(index-1)
#     newNode.next = curNode.next
#     curNode.next.prev = newNode
#     curNode.next = newNode
#     newNode.prev = curNode
#     self.length+=1

#   def remove(self, index):
#     if index < 0:
#       return "error index too small"

#     if index > self.length:
#       return "error index too large"

#     curNode = self.__traverseToIndex(index-1)
#     nodeToRemove = curNode.next
#     curNode.next = nodeToRemove.next
#     nodeToRemove.next.prev = curNode
#     nodeToRemove.next = None
#     nodeToRemove.prev = None
#     self.length-=1
#     return nodeToRemove.value

#   def __traverseToIndex(self, index):
#     curNode = self.head
#     i = 0
#     while i!=index:
#       curNode = curNode.next
#       i+=1
#     return curNode

#   def printList(self):
#     curNode = self.head
#     while curNode is not None:
#       print(curNode.value, end="-->") 
#       curNode = curNode.next
#     print()

#   def printListReverse(self):
#     curNode = self.tail
#     while curNode is not None:
#       print(curNode.value, end="<--")
#       curNode = curNode.prev
#     print()
    


# myLinkedList = DoublyLinkedList(10)
# myLinkedList.append(5)
# myLinkedList.append(16)
# myLinkedList.prepend(1)
# myLinkedList.insert(2,99)
# myLinkedList.printList()
# myLinkedList.remove(2)
# myLinkedList.printList()
# myLinkedList.printListReverse()