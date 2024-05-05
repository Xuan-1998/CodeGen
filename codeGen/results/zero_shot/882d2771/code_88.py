import sys
input = lambda: [int(x) for x in input().split()]
t, l, r = input()

# Step 1: Calculate f(l)
f_l = (l - 1) * l // 2

# Step 2: Initialize the result and the current value of f(n)
res = 0
f_n = f_l

for i in range(1, t+1):
    # Step 3: Calculate the term ti·f(l + i - 1) for each i
    term = (t-i) * f_n % (10**9 + 7)
    
    # Update the result and the current value of f(n)
    res += term
    f_n += i

# Step 4: Subtract l·f(r)
res -= l * f_r % (10**9 + 7)

print(res % (10**9 + 7))
