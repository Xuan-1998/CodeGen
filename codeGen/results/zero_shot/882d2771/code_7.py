import sys

def calculate_f(n):
    # Calculate f(n) using an exponential formula
    return (2 ** n - 1) // (n // 2 + 1)

t, l, r = map(int, input().split())
total_sum = 0
for i in range(l, r + 1):
    total_sum += t * calculate_f(i)
print(total_sum % (10**9 + 7))
