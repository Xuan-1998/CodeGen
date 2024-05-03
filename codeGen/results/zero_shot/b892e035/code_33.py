import sys

T = int(input())
result = []

for _ in range(T):
    n = int(input())
    prob1, num1, num2 = 0, 0, 0
    for _ in range(n):
        prob1, num1, num2 = map(float, input().split())
        result.append(prob1 * (1 - prob1))

print(*result, sep='\n')
