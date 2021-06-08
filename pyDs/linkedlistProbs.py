def cycle_check(node):
  marker1 = node
  marker2 = node

  while marker2 != None and marker2.nextnode != None:

    marker1 = marker1.nextnode
    marker2 = marker2.nextnode.nextnode

    if marker2 == marker1:
      return True

  return False


class Node(object):

  def __init__(self, value):
    self.value = value
    self.nextnode = None

# # -------------------------------------------

def reverse(head):
    
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

# print(a.value)
# print(a.nextnode.value)
# print(b.nextnode.value)
# print(c.nextnode.value)

reverse(a)

print(d.value)
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)

# # ------------------------------------

def nth_to_last_node(n, head):

    left_pointer  = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n-1):
        
        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode

    # Move the block down the linked list
    while right_pointer.nextnode:
        left_pointer  = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer