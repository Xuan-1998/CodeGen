code
t = int(input())  # read the number of test cases
for _ in range(t):
    n, m = map(int, input().split())  # read the initial number and operations
    length = len(str(n))  # calculate the initial length of n
    print(length % (10**9 + 7))  # print the answer modulo 10^9+7
