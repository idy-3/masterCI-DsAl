numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

# def bubbleSort(arr):

#   for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#       if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]

#   return arr

# print(bubbleSort(numbers))

# # -----------------------

# def selectionSort(arr):
#   i = 0
#   min_ = 0
#   while i < len(arr):
#     for j in range(i+1, len(arr)):
#       if arr[j] < arr[min_]:
#         min_ = j
#     arr[i], arr[min_] = arr[min_], arr[i]
#     i+=1
#   return arr

# print(selectionSort(numbers))

# # ------------------------

# def insertionSort(arr):
#   i = 1
#   while i < len(arr):
#     current = arr[i]
#     j = i -1
#     while j >= 0 and current < arr[j]:
#         arr[j+1] = arr[j]
#         j-=1
#     arr[j+1] = current
#     i+=1

#   return arr

# print(insertionSort(numbers))

# # ------------------------

# def merge(left, right):
  
#   result = []
#   iLeft = iRight = 0
#   while iLeft < len(left) and iRight < len(right):
#     if left[iLeft] <= right[iRight]:
#       result.append(left[iLeft])
#       iLeft+=1
#     else:
#       result.append(right[iRight])
#       iRight+=1  

#   result += right[iRight:] + left[iLeft:]
#   return result
    

# def mergeSort(arr):
#   if len(arr) == 1:
#     return arr

#   half = len(arr)//2
#   left=arr[:half]
#   right=arr[half:]

#   return merge(mergeSort(left), mergeSort(right))

# print(mergeSort(numbers))

# # --------------------------

def partition(arr, low, pivot):
    # pivot = high
    i, j = low-1, low

    while j < pivot:
        if arr[j] <= arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1


def quickSort(arr, low=None, high=None):
    if low is None or high is None:
        low, high = 0, len(arr)-1

    if low < high:
        pivot_pos = partition(arr, low, high)

        quickSort(arr, low, pivot_pos - 1)
        quickSort(arr, pivot_pos + 1, high)

    return arr

print(quickSort(numbers))