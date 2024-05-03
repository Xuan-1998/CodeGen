import sys
import math

n = int(sys.stdin.readline())
probs = []
total_distinct_nums = 0

for i in range(n):
    prob1, num1, num2 = map(int, sys.stdin.readline().split())
    probs.append(prob1)
    total_distinct_nums = (num1 + 1) * (num2 - num1 + 1)

prob = 1
for prob1 in probs:
    prob *= prob1 / (total_distinct_nums - 1)

print(round(prob, 6))
