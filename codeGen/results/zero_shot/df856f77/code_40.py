n = int(input())  # read N from stdin
arr = list(map(int, input().split()))  # read array elements from stdin

ops = 0  # initialize operations counter
for i in range(1, n):  # iterate over the array
    diff = arr[i] - arr[i-1]  # calculate difference between consecutive elements
    ops += abs(diff)  # add absolute value of difference to operations counter

print(ops)  # print total number of operations required
