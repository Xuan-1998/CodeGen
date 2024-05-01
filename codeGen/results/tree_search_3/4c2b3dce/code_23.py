def find_AB(s):
    # Initialize state tuple as (AB, BA)
    dp = [False, False]
    
    for char in s:
        if char == 'A':
            dp[0], dp[1] = dp[1], not dp[0]
        elif char == 'B':
            dp[0], dp[1] = not dp[0], dp[0]
        
        # If both conditions are met, print "YES" and break
        if dp[0] and dp[1]:
            print("YES")
            return
        
    # If we reach the end of the string without finding 'AB' and 'BA', print "NO"
    print("NO")

# Read input from stdin
s = input().strip()

# Call the function to solve the problem
find_AB(s)
