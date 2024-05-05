import sys

def get_max_grade():
    n, t = map(int, input().split())
    fraction = float(input())

    max_grade = 0
    remaining_time = t

    for i in range(n - 1, -1, -1):
        dt = 1  # time taken to process each digit (constant)
        if remaining_time >= dt:
            if int((fraction * 10) ** (n - i)) % 10 == 5:  # round up
                max_grade += 0.5
            else:  # round down
                max_grade += int(fraction * 10 ** (n - i))
            remaining_time -= dt
        else:
            break

    return int(max_grade)

print(get_max_grade())
