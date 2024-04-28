n = int(input())  # Read input values for a and b
a, b = bin(int(input(), 2))[2:], bin(n)[2:]  # Convert binary strings to integers

dp = [[0] * (len(a) + len(b)) for _ in range(17)]  # Initialize dp table with zeros

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == '1' and b[j] == '1':
            dp[16][j] += pow(2, i)
        elif a[i] == '0' and b[j] == '0':
            continue
        else:
            dp[16][j] += pow(2, i)

for i in range(len(a) + len(b)):
    for j in range(i):
        if a[i-1] == '1':
            dp[i][j] = (dp[i-1][j % (i+1)] if j > i else 0) + ((int(a[i-1], 2) << (len(b)-j-1)) ^ int(b, 2)) * pow(2, len(b)-j-1)

result = sum(dp[-1])
print(result % (10**9 + 7))
