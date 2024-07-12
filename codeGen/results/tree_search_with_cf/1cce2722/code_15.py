python
import sys
input = sys.stdin.read

def max_points(n, sequence):
    # Step 1: Frequency Count
    max_value = 105
    count = [0] * (max_value + 1)
    for num in sequence:
        count[num] += 1

    # Step 2: State Initialization
    dp = [0] * (max_value + 1)

    # Step 3: Base Cases
    dp[0] = 0
    dp[1] = count[1]

    # Step 4: State Transition
    for x in range(2, max_value + 1):
        dp[x] = max(dp[x-1], dp[x-2] + count[x] * x)

    # Step 5: Result
    return dp[max_value]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

