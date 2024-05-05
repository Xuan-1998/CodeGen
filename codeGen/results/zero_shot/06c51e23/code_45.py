import sys

def solve():
    n, t = map(int, input().split())
    decimal_fraction = float(input())

    max_grade = 0
    while True:
        remaining_time = t
        current_grade = round(decimal_fraction, 3)
        while remaining_time > 0 and not current_grade.is_integer():
            remaining_time -= 1
            current_grade += 0.001
        if remaining_time <= 0:
            break
        max_grade = max(max_grade, int(current_grade))
    print(max_grade)

if __name__ == "__main__":
    solve()
