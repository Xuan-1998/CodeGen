# Step 1: Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Step 2: Calculate the total joy for each possible order of feeding
total_joy = 0

for i in range(n):
    for j in range(i+1):
        if j == i-1:
            total_joy += c[j]
        elif j == i:
            total_joy += b[i]
        else:
            total_joy += a[i]

# Step 3: Print the maximum possible total joy
print(total_joy)
