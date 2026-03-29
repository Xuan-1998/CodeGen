# Step 1: Read the input
n = int(input())
a_values = list(map(int, input().split()))
b_values = list(map(int, input().split()))
c_values = list(map(int, input().split()))

# Step 2: Create a function to calculate the maximum total joy given an order of feeding
def max_total_joy(order):
    total_joy = 0
    for i in range(n):
        if i == 0:
            # First hare: adjacent hares are empty (hungry)
            total_joy += a_values[order[i]]
        elif i == n - 1:
            # Last hare: adjacent hares are not empty (full)
            total_joy += c_values[order[i]]
        else:
            # Middle hare: adjacent hares have one of them full and the other hungry
            if order[i-1] < order[i]:
                # Right adjacent hare is full, left adjacent hare is hungry
                total_joy += b_values[order[i]]
            else:
                # Left adjacent hare is full, right adjacent hare is hungry
                total_joy += a_values[order[i]]
    return total_joy

# Step 3: Use dynamic programming to find the maximum total joy by feeding in different orders
dp = [0] * (1 << n)
for mask in range(1 << n):
    for i in range(n):
        if ((mask >> i) & 1):
            # This hare has been fed, so we need to consider its adjacent hares
            if i == 0:
                dp[mask] = max(dp[mask], dp[mask ^ (1 << i)] + a_values[i])
            elif i == n - 1:
                dp[mask] = max(dp[mask], dp[mask ^ (1 << i)] + c_values[i])
            else:
                # Middle hare: adjacent hares have one of them full and the other hungry
                if ((dp[mask ^ (1 << i-1)]) & (dp[mask ^ (1 << i+1))]):
                    # Both adjacent hares are full, so we need to consider b_values[i]
                    dp[mask] = max(dp[mask], dp[mask ^ (1 << i)] + b_values[i])
                else:
                    # One or both adjacent hares are hungry, so we need to consider a_values[i] or c_values[i]
                    if ((dp[mask ^ (1 << i-1))]) & (a_values[i] > c_values[i]):
                        dp[mask] = max(dp[mask], dp[mask ^ (1 << i)] + a_values[i])
                    else:
                        dp[mask] = max(dp[mask], dp[mask ^ (1 << i)] + c_values[i])

# Step 4: Print the maximum total joy
print(max(dp))
