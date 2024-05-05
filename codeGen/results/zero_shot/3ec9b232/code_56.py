n = int(input())
M = list(map(int, input().split()))
M.sort()

ways = 1
for i in range(1, n):
    if M[i] > M[i-1]:
        ways *= (i+1)
    else:
        ways *= 2

print(ways % (10**9 + 7))
