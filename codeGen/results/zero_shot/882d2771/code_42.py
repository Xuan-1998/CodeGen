# Step 1: Define the variables
t, l, r = map(int, input().split())

# Step 2: Calculate f(n) for all values of n in range(l, r+1)
f_values = [0] * (r - l + 1)
for i in range(1, r - l + 1):
    f_values[i] = min(i, 3)  # Assuming the minimum total number of pairwise comparisons is at most 3

# Step 3: Calculate the value of the expression
result = 0
for i in range(t):
    result += t * (f_values[0] if l == 2 else f_values[1] if l == 3 else f_values[2])

# Step 4: Subtract l·f(r) from the result
result -= l * (r - l)

# Step 5: Calculate the modular value of the result
result %= 10**9 + 7

# Step 6: Print the final answer
print(result)
