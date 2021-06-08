# from pyDs.SQnDeque import Stack

# def balance_check(s):


#   if len(s)%2 != 0:
#     return False

#   opening = set('([{')

#   matches = set([('(',')'), ('[',']'), ('{','}') ])

#   stack = Stack()

#   for paren in s:

#     if paren in opening:
#       stack.push(paren)

#     else:
#       if stack.isEmpty():
#         return False

#       last_open = stack.pop()

#       if (last_open,paren) not in matches:
#         return False

#   return stack.isEmpty()


# print(balance_check("()({})"))
# print(balance_check("()({}])"))

# # ------------------------
# Implement a Queue using 2 stacks

class Queue2Stacks(object):

  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def isEmpty(self):
    return self.stack1 == [] and self.stack2 == []

  def enqueue(self,element):
    self.stack1.append(element)

  def dequeue(self):
    if self.stack1 == [] and self.stack2 == []:
      return None

    if len(self.stack2) == 0:
      for i in range(len(self.stack1)):
        self.stack2.append(self.stack1.pop())

    return self.stack2.pop()  
  

q = Queue2Stacks()

print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())


