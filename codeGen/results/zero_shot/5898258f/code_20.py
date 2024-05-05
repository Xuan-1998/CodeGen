import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, X = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        prefix_sum = [0]
        for a in A:
            prefix_sum.append(prefix_sum[-1] + a)
        
        max_sum = 0
        for i in range(2, N+1):
            for j in range(i-1, -1, -1):
                cur_sum = prefix_sum[i] - prefix_sum[j]
                if X > 0 and (cur_sum % 2) != 0:
                    cur_sum += X
                max_sum = max(max_sum, cur_sum)
        
        print(max_sum)

solve()
