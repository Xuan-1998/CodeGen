import sys

def solve():
    n, t = map(int, input().split())
    decimal_fraction = float(input())

    max_grade = 0
    for i in range(n):
        grade = int(decimal_fraction * (10 ** i))
        if grade >= max_grade and t - i > 0:
            max_grade = grade
            break

    print(max_grade)

if __name__ == "__main__":
    solve()
