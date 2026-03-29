import sys

t, l, r = map(int, input().split())

f_l = 0  # minimal total number of pairwise comparisons needed for girls in group l
for i in range(1, r-l+2):
    f_l += i  # f(i) is the sum of all integers from 1 to i

answer = t * f_l - l * f(r)
print(answer % (10**9 + 7), end='')
