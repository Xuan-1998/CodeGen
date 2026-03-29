import sys

def count_no_consecutive_ones(n):
    dp = [True]  # Initialize dynamic programming array
    for i in range(1, n + 1):
        if not dp[-1]:  # If previous number didn't have consecutive ones
            dp.append(not (i & ((i - 1) // 2)))  # Check if current number has consecutive ones
        else:  # If previous number had consecutive ones
            dp.append(True)  # Current number will also have consecutive ones

    return sum(1 for x in dp if not x)  # Count the numbers with no consecutive ones

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(count_no_consecutive_ones(n))
