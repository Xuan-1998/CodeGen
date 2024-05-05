import math

t, l, r = map(int, input().split())

# Calculate f(n) for each value of n from l to r
f_values = []
for i in range(l, r+1):
    # Initialize variables to store the number of comparisons needed at each level
    left, right = 1, i
    
    # The number of comparisons needed is log2(i)
    comparisons_needed = math.ceil(math.log2(i))
    
    f_values.append(comparisons_needed)

# Calculate the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)
expression_value = sum([t * f for t, f in zip(map(int, str(t)), f_values)]) - (l * f_values[-1])

print(expression_value % (10**9 + 7))
