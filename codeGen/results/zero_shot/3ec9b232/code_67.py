# Step 2: Count the number of pairs
count = 0
for i in range(n):
    for j in range(i+1, n):
        if m[i] < m[j]:
            count += 1

# Step 3: Calculate the result
result = pow(2, count, 10**9 + 7)
print(result)
