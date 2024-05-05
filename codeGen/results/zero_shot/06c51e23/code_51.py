import sys
n, t = map(int, input().split())
fraction = float(input())

# We are given that the fraction will not end with 0, so we don't need to worry about trailing zeroes.
grade = 0.5 * (1 - round(2 ** (-t % n)))

print(int(grade))
