import sys
from collections import namedtuple

T = int(input())

CarryTable = namedtuple('CarryTable', ['total_carries', 'cumulative_sum'])
carry_table = [CarryTable(0, 0) for _ in range(101)]

def calculate_carry_table(n):
    for i in range(1, n+1):
        carry_table[i].total_carries = (i-1)*2
        for j in range(i-1, -1, -1):
            if i-j >= 10:
                carry_table[i].cumulative_sum += carry_table[j].cumulative_sum + (i-j)
            else:
                break

def expected_non_zero_carries(n):
    return carry_table[n].cumulative_sum / ((n+1)*n//2)

for _ in range(T):
    n = int(input())
    calculate_carry_table(n)
    print(expected_non_zero_carries(n))
