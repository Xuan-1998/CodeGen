from collections import defaultdict
from itertools import product

# Initialize the memoization table with default values as 0
dp = defaultdict(int)

def find_max_common_substrings(str1, str2):
    N = len(str1)
    
    # Fill the memoization table
    for i, j in product(range(N+1), range(N+1)):
        if i == j == 0:
            dp[(i, j)] = 0
        else:
            common = (str1[:i+1] == str2[:j+1])
            dp[(i, j)] = max(common and dp.get((i-1, j-1), 0) + 1, dp.get((i-1, j), 0), dp.get((i, j-1), 0))
    
    return dp[(N, N)]

str1, str2 = input().split()
print(find_max_common_substrings(str1, str2))
