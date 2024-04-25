# Read the number of test cases
T = int(input().strip())

# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().strip().split())

    # The answer is the minimum of N and M
    answer = min(N, M)

    # Print the answer for the current test case
    print(answer)
