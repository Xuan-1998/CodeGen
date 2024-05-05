from collections import defaultdict

def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = defaultdict(bool)
        dp[(0, -1)] = True  # base case: starting from an empty sequence
        for i in range(n):
            for j in range(i+1):
                if (i-j) >= b[i]:
                    dp[(n-i-1, b[i])] |= dp.get((j, b[j]), False)
        print('YES' if dp.get((0, -1), False) else 'NO')

can_send_over_network()
