import sys

def prob(n, probs):
    dp = {(0, 0, 0): 1.0}

    for i in range(1, n+1):
        count1, count2 = 0, 0
        p1, num1, num2 = map(float, input().split())
        for k in range(count1, count2+1):
            if (k, count1, count2) not in dp:
                dp[(k, count1, count2)] = dp.get((k-1, count1, count2), 0.0)
            if num1 == num2:
                dp[(k, count1+1, count2)] += p1 * dp.get((k-1, count1, count2), 0.0)
            else:
                dp[(k, count1, count2+1)] += (p1 + (1-p1)/2) * dp.get((k-1, count1, count2), 0.0)

    return round(dp.get((n, 0, 0), 0.0), 6)

T = int(input())
for _ in range(T):
    n = int(input())
    probs = []
    for _ in range(n):
        probs.append(list(map(float, input().split())))
    print(prob(n, probs))
