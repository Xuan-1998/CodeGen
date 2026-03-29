def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    from itertools import combinations
    
    # Number of elements
    num_elements = 2**n
    
    # Initialize dp array
    dp = [set() for _ in range(num_elements + 1)]
    
    # Base case: for i = 0, each subset contains the elements themselves
    for i in range(1, num_elements + 1):
        dp[0].add(i)
    
    # Process each bit in the string s
    for i in range(n):
        next_dp = [set() for _ in range(num_elements + 1)]
        if s[i] == '0':
            for mask in range(1, num_elements + 1):
                for j in range(1, num_elements + 1, 2):
                    if j + 1 <= num_elements:
                        next_dp[mask].add(min(dp[mask].intersection({j, j + 1})))
        else:
            for mask in range(1, num_elements + 1):
                for j in range(1, num_elements + 1, 2):
                    if j + 1 <= num_elements:
                        next_dp[mask].add(max(dp[mask].intersection({j, j + 1})))
        dp = next_dp
    
    # Extract the possible maximum values from the final dp state
    result = list(dp[num_elements])
    result.sort()
    
    # Print the result
    print(" ".join(map(str, result)))


