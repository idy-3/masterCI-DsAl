
# naive
# def has_pair_with_sum(data, sum):
#   d=len(data)

#   for i in range(d-1):
#     for j in range(i+1, d):
#       if data[i]+data[j]==sum:
#         return True
#   return False


# better
# def has_pair_with_sum(data, sum):
#   comp = set()

#   for value in data:
#     if value in comp:
#       return True
#     comp.add(sum-value)
#   return False

# print(has_pair_with_sum([1,2,3,9],8))
# print(has_pair_with_sum([1,2,4,4],8))

# # ---------------------

# array1 = ['a','b', 'c', 'x']
# array2 = ['z','y', 'v']

# def contains_common_item(arr1, arr2):

#   arr_map = set(arr1)

#   for i in arr2:
#     if i in arr_map:
#       return True
#   return False

# print(contains_common_item(array1, array2))

# # -----------------------

# class Player:
#   def __init__(self, name, type_):
#     self.name = name
#     self.type = type_

#   def introduce(self):
#     print(f"Hi I am {self.name}, I am {self.type}")

# class Wizard(Player):
#   def __init__(self, name, type_):
#     super().__init__(name, type_)

#   def play(self):
#     print("WEEEEEEE i'm a %s" % self.type)

# x = Wizard("Mike", "Healer")
# x.introduce()
# x.play()

# # --------------------------------

# from Ds import arrays
# from Ds import hashTable
# from Ds import exercise
# from Ds import linkedList
# from Ds import stack
# from Ds import queue
# from Ds import trees
# from Ds import graphs

# from Al import recursion
# from Al import sorting
# from Al import BFSnDFS


# from pyDs import dynamicArray
# from pyDs import arrayProbs
# from pyDs import SQnDeque
# from pyDs import dequeProbs
# from pyDs import linkedlistProbs
# from pyDs import recursiveProbs
from pyDs import Tree


