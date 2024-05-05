import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())
    prefix_sum = [0]
    
    for sign in signs:
        if sign == '+':
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(prefix_sum[-1] - 1)
    
    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = sum(prefix_sum[l:r+1])
        if left_sum % 2 == 0:
            print(0)  # No need to remove any elements
        else:
            count = (left_sum // -1 + 1)
            print(count)

solve()
