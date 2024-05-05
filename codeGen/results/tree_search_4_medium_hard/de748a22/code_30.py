import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    prefix_sum = 0
    suffix_sum = 0
    state = 0

    for i in range(n):
        if signs[i] == "+":
            state += 1
        else:
            state -= 1
        prefix_sum += 1 if signs[i] == "+" else -1
        suffix_sum += 1 if signs[n-i-1] == "+" else -1

    for _ in range(q):
        l, r = map(int, input().split())
        removed = state
        for i in range(l):
            if signs[i] == "+":
                state -= 1
            else:
                state += 1
        prefix_sum -= sum(1 if signs[i] == "+" else -1 for i in range(l))
        suffix_sum -= sum(1 if signs[n-i-1] == "+" else -1 for i in range(r, n))

        for i in range(l, r+1):
            if signs[i] == "+":
                state -= 1
            else:
                state += 1

        print(min(removed, state))
