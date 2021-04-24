import json

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    newNode = Node(value)
    if self.root is None:
      self.root = newNode
    else:
      curNode = self.root
      while True:
        if newNode.value < curNode.value:
          if curNode.left is None:
            curNode.left = newNode
            return 
          curNode = curNode.left
        else:
          if curNode.right is None:
            curNode.right = newNode
            return 
          curNode = curNode.right
        
  def lookup(self, value):
    if self.root is None:
      return False
    curNode = self.root
    while curNode is not None:
      if value == curNode.value:
        return curNode.value
      elif value < curNode.value:
        curNode = curNode.left
      elif value > curNode.value:
        curNode = curNode.right
    return False

  def remove(self, value):
    if self.root is None:
      return False

    curNode = self.root
    parentNode = None
    while curNode is not None:
      if value < curNode.value:
          parentNode = curNode
          curNode = curNode.left
      elif value > curNode.value:
          parentNode = curNode
          curNode = curNode.right
      elif value == curNode.value:
          # option 1: No right child
          if curNode.right is None:
              if parentNode is None:
                  self.root = curNode.left
              else:
                  # if parent < current value, make left child a right child of parent
                  if curNode.value < parentNode.value:
                      parentNode.left = curNode.left
                  # if parent < current value, make left child a right child of parent
                  elif curNode.value > parentNode.value:
                      parentNode.right = curNode.left
          # Option 2: Right child which doesnt have a left child
          elif curNode.right.left is None:
              curNode.right.left = curNode.left
              if parentNode is None:
                  self.root = curNode.right
              else:
                  # if parent > current, make right child of the left the parent
                  if curNode.value < parentNode.value:
                      parentNode.left = curNode.right
                  # if parent < current, make right child a right child of the parent
                  elif curNode.value > parentNode.value:
                      parentNode.right = curNode.right
          # Option 3: Right child that has a left child
          elif curNode.right is not None and curNode.right is not None:
              # find the Right child's left most child
              leftmost = curNode.right.left
              leftmostParent = curNode.right
              while leftmost.left is not None:
                  leftmostParent = leftmost
                  leftmost = leftmost.left

              # Parent's left subtree is now leftmost's right subtree
              leftmostParent.left = leftmost.right
              leftmost.left = curNode.left
              leftmost.right = curNode.right

              if parentNode is None:
                  self.root = leftmost
              else:
                  if curNode.value < parentNode.value:
                      parentNode.left = leftmost
                  elif curNode.value > parentNode.value:
                      parentNode.right = leftmost
          # Option 4 : No Left Child But Got Right Child
          else:
              if parentNode is None:
                  self.root = curNode.right
              else:
                  if curNode.value < parentNode.value:
                      parentNode.left = curNode.right
                  elif curNode.value > parentNode.value:
                      parentNode.right = curNode.right

          return True

  def BreadthFirstSearch(self):
    curNode = self.root
    arr = []
    queue = []
    queue.append(curNode)

    while len(queue) > 0:
      curNode = queue.pop(0)
      arr.append(curNode.value)
      if curNode.left is not None:
        queue.append(curNode.left)
      if curNode.right is not None:
        queue.append(curNode.right)
    return arr

  def BreadthFirstSearchRecursive(self, queue=None, arr=None):
    if queue is None and arr is None:
      queue = [self.root]
      arr = []

    if len(queue) == 0:
      return arr

    curNode = queue.pop(0)
    arr.append(curNode.value)
    if curNode.left is not None:
      queue.append(curNode.left)
    if curNode.right is not None:
      queue.append(curNode.right)

    return self.BreadthFirstSearchRecursive(queue, arr)

  def DFSInorder(self, curNode=None, arr=None):
    if curNode is None and arr is None:
      curNode = self.root
      arr = []

    if curNode.left is not None:
      self.DFSInorder(curNode.left, arr)
    arr.append(curNode.value)
    if curNode.right is not None:
      self.DFSInorder(curNode.right, arr)
    return arr
        
  def DFSPostorder(self, curNode=None, arr=None):
    if curNode is None and arr is None:
      curNode = self.root
      arr = []

    if curNode.left is not None:
      self.DFSPostorder(curNode.left, arr)
    if curNode.right is not None:
      self.DFSPostorder(curNode.right, arr)
    arr.append(curNode.value)
    return arr

  def DFSPreorder(self, curNode=None, arr=None):
    if curNode is None and arr is None:
      curNode = self.root
      arr = []

    arr.append(curNode.value)
    if curNode.left is not None:
      self.DFSPreorder(curNode.left, arr)
    if curNode.right is not None:
      self.DFSPreorder(curNode.right, arr)
    return arr

#      9
#   4    20
# 1  6  15  120

tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.remove(170)
# print(tree.lookup(21))
# json.dumps(traverse(tree.root))

# print(tree.__dict__)

def traverse(node):
  tree = { "value": node.value, "left": None, "right": None }
  tree["left"] =  None if node.left is None else traverse(node.left)
  tree["right"] =  None if node.right is None else traverse(node.right)
  return tree

# print(json.dumps(traverse(tree.root)))
# print('BFS', tree.BreadthFirstSearch())
# print('BFS', tree.BreadthFirstSearchRecursive())
print('DFSInorder', tree.DFSInorder())
print('DFSPostorder', tree.DFSPostorder())
print('DFSPreorder', tree.DFSPreorder())