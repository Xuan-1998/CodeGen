import sys

def find_sums(a):
    n = len(a)
    max_sum = sum(a)
    
    # Initialize a dictionary to store the intermediate results.
    dp = {0: 1}
    sums = []
    
    for s in range(1, max_sum + 1):
        if s <= n:
            dp[s] = 1
        else:
            for i in range(s):
                if i in dp and (s - i) in dp:
                    dp[s] = 1
                    break
    
    # Add the sums to the list.
    for s in sorted(dp.keys()):
        sums.append(s)
    
    return ' '.join(map(str, sums))

# Read input from stdin.
N = int(input())
a = [int(x) for x in input().split()]

print(find_sums(a))
