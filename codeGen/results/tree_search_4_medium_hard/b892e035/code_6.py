from functools import lru_cache

@lru_cache(None)
def solve(i, prev_p1, prev_p2):
    if i == 0:  # base case: all tickets used
        return prev_p1 * prev_p2
    else:
        p = 0.0  # initialize total probability
        for p1 in range(100):  # iterate over possible probabilities of the first number
            for p2 in range(100):  # iterate over possible probabilities of the second number
                if (p1, p2) == (prev_p1, prev_p2):  # skip repeated numbers
                    continue
                new_p1 = min(p1 + 1, 99)  # update probability of the first number
                new_p2 = min(p2 + 1, 99)  # update probability of the second number
                p += (p1 * prev_p1 * p2 * prev_p2) / (100.0 ** i)  # calculate probability for this case
        return p

T = int(input())  # read number of test cases
for _ in range(T):
    n = int(input())  # read number of tickets
    prob = [list(map(int, input().split())) for _ in range(n)]  # read probabilities and numbers
    print(solve(n, *prob[0], 1))  # calculate probability and print
