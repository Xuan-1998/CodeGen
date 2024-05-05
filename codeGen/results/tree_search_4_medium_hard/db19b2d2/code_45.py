import sys

# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Initialize an array pmf[1...n] with all zeros.
pmf = [0.0] * (n + 1)

# Calculate the probability mass function (PMF) recursively.
for i in range(1, m + 1):
    for p in range(h, n + 1):
        if p >= s[i - 1]:
            pmf[p] += s[i - 1] / sum(s)
        else:
            pmf[p] = pmf[p]

# Calculate the desired probability PMF(n) as the sum of all probabilities greater than or equal to 1.
pmf_n = sum(pmf[k] for k in range(h, n + 1))

print(pmf_n)
