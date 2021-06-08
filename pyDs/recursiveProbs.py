# def rec_sum(n):
#   if n == 0:
#     return 0

#   return n + rec_sum(n-1)


# print(rec_sum(4))

# # -----------------------

# def sum_func(n):
#   if n == 0:
#     return 0

#   return n % 10 + sum_func(n//10)

# print(sum_func(4321))
# print(sum_func(4502))

# # ----------------------------


# def word_split(phrase, list_of_words, output = None):

#   if output is None:
#     output = []

#   for word in list_of_words:

#     # if phrase.startswith(word):
#     if phrase[:len(word)] == word:
#       output.append(word)

#       return word_split(phrase[len(word):], list_of_words, output)

#   return output


# print(word_split('themanran',['the','ran','man']))
# print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
# print(word_split('themanran',['clown','ran','man']))


# # --------------------------------------------------

# def reverse(s):

#   if s == "":
#     return ""
#   else:
#     return s[-1] + reverse(s[:-1]) 
  

# print(reverse('hello world'))

# # ---------------------------

# def permute(s):
    
#   out = []

#   if len(s) == 1:
#     out = [s]
#   else:
#     for i, char in enumerate(s):
#       print('char', char)
#       for perm in permute(s[:i] + s[i+1:]):
#         print('perm', perm)
#         out += [char+perm]
#         print('char+perm', char+perm)
#         print('out', out)


#   return out

# print(permute('abc'))

# permute 2

# def permute2(s, out=None):
  
#   if out is None:
#     out = ""

#   if len(s) == 0:
#     print(out)
#     return out

#   for i in range(len(s)):
#     ch = s[i]
#     qlpart = s[:i]
#     qrpart = s[i+1:]
#     roq = qlpart + qrpart
#     permute(roq, out+ch)

# print(permute2('abc'))

# # -------------------------

# def fib(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n in memo.keys():
#         return memo[n]
#     if n <= 2:
#         return 1
#     memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]


# print(fib(6))  # 8
# print(fib(7))  # 13
# print(fib(8))  # 21
# print(fib(50))  # 12586269025

# # ----------------------

# def rec_coin(target, coins, memo=None):
#   min_coins = target
#   if memo is None:
#     memo = {}
  
#   if target in coins:
#     memo[target] = 1
#     return 1

#   elif target in memo.keys():
#     return memo[target]

#   else:
#     for i in [c for c in coins if c<= target]:
#       num_coins = 1+ rec_coin(target-i,coins,memo)

#       if num_coins < min_coins:
#         min_coins = num_coins

#         memo[target] = min_coins

#   return min_coins


# print(rec_coin(10,[1,5]))
# print(rec_coin(74,[1,5,10,25]))

# # ---------------------------

def coin_change(amount, coins):
  coins.sort()
  dp = [amount+1]*(amount+1)
  # print(dp)
  dp[0] = 0
  for i in range(amount+1):
    for j in range(len(coins)):
      if coins[j] <= i:
        dp[i] = min(dp[i], 1 + dp[ i-coins[j] ])
      else:
        break
  print(dp)  
  return -1 if dp[amount] > amount else dp[amount]

# print(coin_change(74,[1,5,10,25]))
print(coin_change(10,[1,5]))
# print(coin_change(11,[1,2,5]))
# print(coin_change(63,[1,2,5]))
print(coin_change(12,[1,2,5]))
