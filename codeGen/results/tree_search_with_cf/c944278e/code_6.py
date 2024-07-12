python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Number of elements in the sequence
    length = 2 ** n
    
    # DP table
    dp = [set() for _ in range(length)]
    
    # Initialize base case
    for mask in range(length):
        dp[mask] = {mask + 1}
    
    # Iterate over each bit in the string s
    for i in range(n):
        next_dp = [set() for _ in range(length)]
        for mask in range(0, length, 2):
            for x in dp[mask]:
                for y in dp[mask + 1]:
                    if s[i] == '0':
                        next_dp[mask // 2].add(min(x, y))
                    else:
                        next_dp[mask // 2].add(max(x, y))
        dp = next_dp
    
    # The result is in dp[0]
    result = sorted(dp[0])
    print(" ".join(map(str, result)))


