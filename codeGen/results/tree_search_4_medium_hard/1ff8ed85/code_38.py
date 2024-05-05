import heapq

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        a = []
        state_dict = {}
        memo = {}
        for i in range(1, n+1):
            if (i, 0) not in memo:
                dp(a, b[:i])
            if any(state_dict.values()):
                print('YES')
                break
        else:
            print('NO')

def dp(a, b):
    if tuple(b) in memo:
        return memo[tuple(b)]
    n = len(b)
    res = True
    for i in range(n-1):
        if int(str(i+1) + str(len(str(b[i])))) not in b:
            res = False
            break
        segment_len = 1
        while i + segment_len <= n and a == [str(j) for j in range(i, i+segment_len)]:
            segment_len += 1
        if str(segment_len) not in b or segment_len > len(str(b[0])):
            res = False
            break
    memo[tuple(b)] = res
    return res

if __name__ == '__main__':
    solve()
