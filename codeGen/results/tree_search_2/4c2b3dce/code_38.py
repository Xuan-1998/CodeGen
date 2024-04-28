def find_AB(s):
    n = len(s)
    
    # Initialize dp array to store the count of 'A' and 'B'
    dp = [False] * (n + 1)
    a_count = b_count = 0
    
    for i in range(1, n + 1):
        if s[i - 1] == 'A':
            a_count += 1
        else:
            b_count += 1
        
        # Update dp array based on the count of 'A' and 'B'
        if a_count > b_count:
            dp[i] = True
        elif a_count < b_count:
            dp[i] = False
    
    # Check if both substrings "AB" and "BA" are present in the string
    has_AB = any(s[i:i + 2] == "AB" for i in range(n - 1))
    has_BA = any(s[i:i + 2] == "BA" for i in range(n - 1))
    
    return "YES" if (dp[-1] and (has_AB or has_BA)) else "NO"

# Read input from stdin
s = input()

print(find_AB(s))
