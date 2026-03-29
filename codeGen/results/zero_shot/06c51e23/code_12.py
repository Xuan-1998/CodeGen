import sys

def solve():
    n, t = map(int, input().split())
    decimal_fraction = float(input())

    # Initialize the maximum grade and the current time
    max_grade = 0
    current_time = 0

    # Iterate through the decimal fraction from right to left
    for i in range(n-1, -1, -1):
        # Calculate the time needed to round this digit
        time_needed = min(9, t // (10 ** (n - i - 1)))
        current_time += time_needed

        # If we have enough time to round this digit, do it and update the maximum grade
        if current_time <= t:
            if decimal_fraction % 10 >= 5:
                max_grade = int(decimal_fraction) + 1
                break
            else:
                max_grade = int(decimal_fraction)
        else:
            # If we don't have enough time to round this digit, stop here and use the current grade
            max_grade = int(decimal_fraction)
            break

    print(max_grade)

if __name__ == "__main__":
    solve()
