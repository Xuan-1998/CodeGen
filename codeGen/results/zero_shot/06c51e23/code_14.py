import sys

def solve():
    n, t = map(int, input().split())
    fraction = float(input())

    max_grade = 0
    for i in range(2 ** n):
        rounded_fraction = round(fraction, int(i).bit_length() - 1)
        grade = int(rounded_fraction * 100) // 1
        if grade > max_grade and t >= (i + 1) * 10:  # adjust the time limit
            max_grade = grade

    print(max_grade)

if __name__ == "__main__":
    solve()
