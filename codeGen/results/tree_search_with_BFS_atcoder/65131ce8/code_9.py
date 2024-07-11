from sys import stdin, stdout
from operator import mul
from functools import reduce
import itertools

MOD = 998244353
N = int(stdin.readline().strip())
D = list(map(int, stdin.readline().strip().split()))
D.insert(0, 0)

if D[1] != 1 or D[0] != 0:
    print(0)
else:
    cnt = [0] * (N+1)
    for i in range(2, N+1):
        cnt[D[i]] += 1
        
    ans = 1
    sumD = 1
    for i in range(1, N):
        ans = ans * pow(cnt[i], D[i+1], MOD) % MOD * reduce(mul, range(1, D[i+1]+1), 1) % MOD
        sumD += D[i+1]
        if sumD > i+1:
            print(0)
            break
    else:
        print(ans)

