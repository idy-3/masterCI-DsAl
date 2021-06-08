# def anagram(s1, s2):

#   s1 = s1.lower().replace(' ', '')
#   s2 = s2.lower().replace(' ', '')

#   if len(s1) != len(s2):
#     return False

#   bank = {}

#   for i in s1:
#     if i not in bank:
#       bank[i] = 1
#     else:
#       bank[i] += 1

#   for i in s2:
#     if i in bank:
#       bank[i] -= 1
#       if bank[i] <= 0:
#         bank.pop(i)

#   return True if len(bank) == 0 else False


# print(anagram("God","Dog"))
# print(anagram("clint eastwood","old west action"))

# # -----------------------
# Array pair sum

# def pair_sum(arr,k):

#   if len(arr) <= 1:
#     return arr

#   bank = {}
#   result = set()
#   for i in arr:
#     bank[k-i] = i
#     if i in bank:
#       if i < bank[i]:
#         result.add((i, bank[i]))
#       else:
#         result.add((bank[i], i))
      

#   return len(result)


# print(pair_sum([1,3,2,2],4))
# print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
# print(pair_sum([1,2,3,1],3))

# # -----------------------
# Find the missing element

# def finder(arr1, arr2):
# # O(nlog(n))
#   if len(arr1) == 0 or len(arr2) == 0:
#     return

#   arr1 = sorted(arr1)
#   arr2 = sorted(arr2)

#   for i,j in zip(arr1, arr2):
#     if i != j:
#       return i
#   return "equal"

# solution 2

# def finder(arr1, arr2):
# # O(n)
#   bank = {}

#   for i in arr2:
#     if i in bank:
#       bank[i] += 1
#     else:
#       bank[i] = 1

#   for i in arr1:
#     if bank.get(i,0) == 0:
#       return i
#     else:
#       bank[i] -= 1

# print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
# print(finder([5,5,7,7], [5,7,7]))
# print(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

# # -----------------------
# Largest Continuous Sum

# def largest_cont_sum(arr):
#   if len(arr)==0:
#     return 0

#   max_sum = current_sum = arr[0]

#   for i in arr[1:]:
#     current_sum = max(current_sum+i,i)
#     max_sum = max(current_sum,max_sum)

#   return max_sum

# print(largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

# # -----------------------
# Sentence Reversal

# def rev_word(s):
#   s = s.strip().split()

#   return " ".join(reversed(s))

# solution 2

# def rev_word(s):
  
#   words = []
#   length = len(s)

#   i = 0

#   while i < length:
#     if s[i] != " ":
#       word_start = i
#       while i < length and s[i] != " ":
#         i+=1
#       words.append(s[word_start:i])

#     i+=1

#   reverseWords = []
#   for x in range(len(words)):
#     reverseWords.append(words.pop())

#   return " ".join(reverseWords)


# print(rev_word('    space before'))
# print(rev_word('Hi John,   are you ready to go?'))

# # -----------------------
# String Compression

# def compress(s):

#   bank = {}
#   fin = []

#   for i in s:
#     if i in bank:
#       bank[i] += 1
#     else:
#       bank[i] = 1

#   for i,j in bank.items():
#     # print(i)
#     fin.append(f"{i}{int(j)}")

#   return "".join(fin)


# def compress(s):

#   run = ""

#   if len(s) == 0:
#     return ""

#   if len(s) == 1:
#     return s+"1"

#   cnt = i =1
#   while i < len(s):
#     if s[i] == s[i-1]:
#       cnt +=1
#     else:
#       run = run + s[i-1] + str(cnt)
#       cnt = 1

#     i+=1
#   run = run + s[i-1] + str(cnt)

#   return run

# print(compress("AAAAABBBBCCCC"))


# # -----------------------
# Unique Characters in Sting

def uni_char(s):
  bank = set()

  for i in s:
    if i in bank:
      return False
    else:
      bank.add(i)

  return True

print(uni_char('abcdefg'))
print(uni_char('goo'))