import math

def solution(n):
    # Calculate the number of ways to choose n towns with replacement (i.e., each town can be chosen multiple times)
    total_ways = 2 ** n
    
    # Calculate the number of ways to choose exactly one tower per town without repetition
    choose_town = math.comb(n + 1, n)  # Choose n+1 towns and select n of them
    
    # Calculate the probability
    prob = (total_ways // choose_town) % 998244353
    
    return prob

n = int(input())
print(solution(n))
