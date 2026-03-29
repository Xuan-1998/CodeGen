from collections import defaultdict

def query_sign_variable_sum(signs, left, right):
    positive = 0
    negative = 0
    for sign in signs[left:right+1]:
        if sign == '+':
            positive += 1
        else:
            negative += 1
    return positive - negative

def min_removals_to_zero_sign_variable_sum(signs, queries):
    dp = defaultdict(int)
    
    n = len(signs)
    for i in range(n):
        dp[(0, i)] = 0
    
    for query in queries:
        l, r = query
        sign_variable_sum = query_sign_variable_sum(signs, l-1, r)
        
        if sign_variable_sum == 0:
            print(0)  # No elements need to be removed
        else:
            min_removals = float('inf')
            for i in range(l, r+1):
                j = i
                while j <= r and signs[j] != '+':
                    j += 1
                if j > l:
                    sign_variable_sum -= 2*(j-l)
                    min_removals = min(min_removals, dp[(l, j-1)])
            print(min_removals)

min_removals_to_zero_sign_variable_sum(input().split(), list(map(int, input().split())))
