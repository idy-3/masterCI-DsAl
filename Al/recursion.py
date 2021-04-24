# def findFactorialRecursive(number):
#   if number == 1:
#     return 1
#   answer = number * findFactorialRecursive(number - 1)
#   return answer

# def findFactorialIterative(number):
#   answer = 1
#   for i in range(number,1,-1):
#     answer *= i
#   return answer

# print(findFactorialRecursive(5))
# print(findFactorialIterative(5))

# # --------
# fibonacci 

# def fibonacciIterative(n):
#   arr = [0,1]
#   for i in range(2, n+1):
#     arr.append(arr[i-2]+ arr[i-1])
#   return arr[n]

# def fibonacciRecursive(n):
#   if n < 2:
#     return n  
#   return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)

# print(fibonacciIterative(43))
# print(fibonacciRecursive(30))

# # ---------
def reverseString(string):
  return string[-1::-1]


def reverseStringRecursive(string):
  if string == "":
    return ""
  else:
    return reverseStringRecursive(string[1:]) + string[0]

  

print(reverseString('yoyo mastery'))
print(reverseStringRecursive('yoyo mastery'))

