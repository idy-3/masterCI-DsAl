# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

# Given an array = [2,3,4,5]
# It should return None

#naive (n^2)
# def firstRecurringChar(arr):
#   for i in range(1, len(arr)):
#     j = i-1
#     while j>=0:
#       if arr[i] == arr[j]:
#         return arr[i]
#       j-=1

def firstRecurringChar(arr):
  h = set()
  for i in arr:
    if i in h:
      return i
    h.add(i)
  return None

print(firstRecurringChar([2,5,1,2,3,5,1,2,4]))
print(firstRecurringChar([2,1,1,2,3,5,1,2,4]))
print(firstRecurringChar([2,3,4,5]))
print(firstRecurringChar(["a","A","a","b"]))
print(firstRecurringChar([2,1,1,2,3]))
