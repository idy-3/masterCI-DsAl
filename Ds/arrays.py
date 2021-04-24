# class MyArray:
#   def __init__(self):
#     self.length = 0;
#     self.data = {}

#   def get(self, index):
#     return self.data[index]

#   def push(self, item):
#     self.data[self.length] = item
#     self.length +=1
#     return self.length

#   def pop(self):
#     last_item = self.data[self.length-1]
#     del self.data[self.length-1]
#     self.length -= 1
#     return last_item

#   def delete(self, index):
#     item = self.data[index]
#     self.shift_items(index)
#     return item

#   def shift_items(self, index):
#     for i in range(index, self.length-1):
#       self.data[i] = self.data[i+1]
#     del self.data[self.length-1]
#     self.length-=1


# newArray = MyArray()
# newArray.push('Hi')
# newArray.push('You')
# newArray.push('!')
# newArray.delete(0)
# newArray.push('are')
# newArray.push('nice')
# newArray.delete(1)

# print(newArray.__dict__)

# # ------------------------------

# def mergeSortedArrays(arr1, arr2):
  
#   if len(arr1)==0 or len(arr2) ==0:
#     return arr1 + arr2


#   mergedArray = []
#   arr1_index = arr2_index = 0

#   while len(mergedArray) < len(arr1)+len(arr2):
#     if arr1[arr1_index] <= arr2[arr2_index]:
#       mergedArray.append(arr1[arr1_index])
#       arr1_index +=1
#     else:
#       mergedArray.append(arr2[arr2_index])
#       arr2_index+=1

#     if arr1_index == len(arr1):
#       mergedArray += arr2[arr2_index:]
#       break
    
#     if arr2_index == len(arr2):
#       mergedArray += arr1[arr1_index:]
#       break

#   return mergedArray

# print(mergeSortedArrays([0,3,4,31], [4,6,22,30]))