# We first define the modulo value as 10^9 + 7
mod = 1000000007

def solve():
    n = int(input()) # Read the length of the array
    a = list(map(int, input().split())) # Read the array itself
    
    # Initialize the result as 1 (because the empty subsequence is good)
    res = 1
    
    for i in range(n):
        # If a[i] is not divisible by i + 1, then there's no way to create a good subsequence ending at a[i]
        if (a[i] % (i + 1)) != 0:
            break
        # Otherwise, we increment the result by the number of ways to choose the next element in the subsequence
        res = (res * (n - i)) % mod
    
    print(res)
