import sys
from math import ceil, floor

def find_max_grade():
    n = int(sys.stdin.readline())
    t = int(sys.stdin.readline())
    fraction = float(sys.stdin.readline())

    # Remove trailing zeroes from the decimal fraction
    fraction = str(fraction).rstrip('0').rstrip('.')

    max_grade = 0
    seconds_used = 0

    for i in range(len(fraction)):
        if seconds_used + len(str(fraction[:i+1])) > t:
            break
        grade = floor(10**len(str(fraction)[:i]) * float(fraction[:i]))
        if seconds_used + len(str(grade)) <= t:
            max_grade = max(max_grade, grade)
            seconds_used += len(str(grade))
        else:
            break

    print(max_grade)

if __name__ == "__main__":
    find_max_grade()
