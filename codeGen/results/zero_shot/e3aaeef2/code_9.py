t = int(input())  # Read the number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # Read the initial number and operations
    print(solve(n, m))  # Print the length of the resulting number modulo 10^9+7
