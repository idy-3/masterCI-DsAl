# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

# class Stack:
#   def __init__(self):
#     self.top = None
#     self.bottom = None
#     self.length = 0

#   def peek(self):
#     if self.top is None:
#       return None
#     return self.top.value

#   def push(self, value):
#     newNode = Node(value)
#     if self.top is None:
#       self.top = newNode
#       self.bottom = newNode
#     else:
#       newNode.next = self.top
#       self.top = newNode
#     self.length+=1
 
#   def pop(self):
#     if self.top is None:
#       return None
#     if self.top == self.bottom:
#       self.bottom = None
#     temp = self.top
#     self.top = temp.next
#     temp.next = None
#     self.length-=1
#     return temp.value

#   def isEmpty(self):
#     if self.top is None:
#       return True
#     return False

#   def printList(self):
#     curNode = self.top
#     while curNode is not None:
#       print(curNode.value, end="-->")
#       curNode = curNode.next
#     print()


# myStack = Stack()
# myStack.push(1)
# myStack.push(3)
# myStack.push(9)
# myStack.printList()
# myStack.push(99)
# print(myStack.peek())
# myStack.printList()
# myStack.pop()
# myStack.pop()
# myStack.printList()

# # ------------------
# Stacks With Arrays

class Stack:
  def __init__(self):
    self.array = []

  def peek(self):
    if len(self.array) == 0:
      return None
    return self.array[len(self.array) - 1]

  def push(self, value):
    self.array.append(value)
    return self.array
 
  def pop(self):
    self.array.pop(len(self.array) - 1)

  def isEmpty(self):
    if len(self.array) == 0:
      return True
    return False



myStack = Stack()
myStack.push(1)
myStack.push(3)
myStack.push(9)
myStack.push(99)
print(myStack.peek())
myStack.pop()
print(myStack.__dict__)