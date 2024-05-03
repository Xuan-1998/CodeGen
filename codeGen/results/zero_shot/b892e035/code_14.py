import sys

def get_probability():
    n = int(sys.stdin.readline())
    total_probability = 1.0
    for _ in range(n):
        p1, num1, num2 = map(float, sys.stdin.readline().split())
        probability = p1 * (1 - p1) / ((num1 != num2) + 1e-6)
        total_probability *= probability
    return total_probability

T = int(sys.stdin.readline())
for _ in range(T):
    print(get_probability())
