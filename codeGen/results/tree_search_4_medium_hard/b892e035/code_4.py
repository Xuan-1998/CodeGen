import sys

def correct_numbering_prob(T):
    for _ in range(T):
        n = int(input())
        dp = {(0, set()): 1.0}
        for i in range(1, n+1):
            p1, num1, num2 = map(float, input().split())
            used = dp[(i-1, set())].copy()
            prob = (p1 * (num1 not in used)) + ((1-p1) if num1 in used else 0.0)
            prob += (p2 * (num2 not in used)) + ((1-p2) if num2 in used else 0.0)
            dp[(i, used)] = prob
        print(dp.popitem()[1])

T = int(input())
correct_numbering_prob(T)

