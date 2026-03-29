from sys import stdin

q = int(stdin.readline())
dp = [False] * (2**30)
dp[0] = True

for _ in range(q):
    u, v = map(int, stdin.readline().split())
    
    while v > 0:
        if dp[v ^ u]:
            print("YES")
            break
        v ^= u
    
    else:
        print("NO")
