import math
import sys

T = int(input())  # Read T test cases
probabilities = []
for _ in range(T):
    n = int(input())  # Read number of tickets for this test case
    probs = []  # Store probabilities for this test case
    for _ in range(n):
        P, A, B = map(int, input().split())  # Read probability and numbers for this ticket
        prob = (P / 100) * math.comb(16, n - 1)
        probs.append(prob)
    probabilities.append(max(probs))  # Store maximum probability for this test case

for prob in probabilities:
    print(prob)  # Print probability for this test case
