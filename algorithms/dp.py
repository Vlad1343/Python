 
## Dynamic Programming (DP) Algorithms

## Python program to find fibonacci number using recursion.
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# if __name__ == "__main__":
#     n = 7
#     print(fib(n))




## Python program to find fibonacci number using memoization.
# def fibRec(n, memo):

#     if n <= 1:
#         return n

#     # To check if output already exists
#     if memo[n] != -1:
#         return memo[n]

#     # Calculate and save output for future use
#     memo[n] = fibRec(n - 1, memo) + \
#               fibRec(n - 2, memo)
#     return memo[n]

# def fib(n):
#     memo = [-1] * (n + 1)
#     return fibRec(n, memo)

# n = 5
# print(fib(n))




## Python program to find fibonacci number using tabulation.
# def fibo(n):
#     dp = [0] * (n + 1)

#     # Storing the independent values in dp
#     dp[0] = 0
#     dp[1] = 1

#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
    
#     return dp[n]

# n = 15
# print(fibo(n))





## Python program to find fibonacci number using space optimised.
# def fibo(n):
#     prevPrev, prev, curr = 0, 1, 1

#     for i in range(2, n + 1):
#         curr = prev + prevPrev
#         prevPrev = prev
#         prev = curr

#     return curr

# n = 5
# print(fibo(n))



