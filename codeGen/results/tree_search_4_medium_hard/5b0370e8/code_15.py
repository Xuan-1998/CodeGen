import sys

state = {0: 1}
MOD = 10**9 + 7

def dp(i):
    if i < 0:
        return False
    
    res = state.get(i, -1)
    if res != -1:
        return res == 0
    
    ans = 0
    for j in range(2**k):  
        flag = True
        and_val = j
        xor_val = 0
        for p in range(i+1):
            new_xor_val = (xor_val ^ arr[p])
            new_and_val = (and_val & arr[p])
            if new_xor_val >= new_and_val:
                flag = False
                break
        if flag:
            ans += dp(i-1)
    state[i] = 0 if ans == 0 else 1
    return state[i]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = dp(n-1)
    print(res % MOD)
