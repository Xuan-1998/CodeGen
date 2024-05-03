import math

T = int(input())  # read T test cases
for _ in range(T):
    n = int(input())  # read number of tickets
    probs = []  # store probabilities for each ticket
    for i in range(n):
        p, a, b = map(int, input().split())  # read probability and numbers for the i-th ticket
        probs.append(p)  # add probability to the list
    prob = math.prod([1 - x for x in probs])  # calculate the product of probabilities (1 - p_i)
    print(round(prob, 6))  # print the answer with rounding error less than 10^-6
