# Step 1: Receive inputs A and B
A = int(input())
B = int(input())

# Step 2: Find the largest power of 2 that divides both A and B
power = 0
while (1 << power) <= min(A, B):
    if ((1 << power) & A) and ((1 << power) & B):
        power += 1

# Step 3: Calculate X as the sum of powers of 2 up to the calculated power
X = 0
for i in range(power, -1, -1):
    X |= (1 << i)

# Step 4: Calculate Y by subtracting X from A and then doing XOR with B
Y = A - X
while Y & B:
    Y ^= B

print(X, Y)
