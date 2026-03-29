n = int(input())  # read n from stdin
costs = [int(input()) for _ in range(n)]  # read costs of reversing each string
strings = [input() for _ in range(n)]  # read the strings

# Initialize the minimum total cost and the current position
min_cost = float('inf')
curr_pos = 0

for i in range(2**n):  # iterate over all possible permutations of strings
    permuted_strings = [''] * n  # initialize an array to store the permuted strings
    for j in range(n):
        if (i >> j) & 1:  # check if the jth string should be reversed
            permuted_strings[j] = strings[j][::-1]  # reverse the jth string
        else:
            permuted_strings[j] = strings[j]

    # Check if the permuted strings are in lexicographical order
    is_sorted = True
    for k in range(n - 1):
        if permuted_strings[k].endswith(permuted_strings[k+1]):
            break
    else:
        is_sorted = False

    if is_sorted and curr_pos > min_cost:  # update the minimum total cost if needed
        min_cost = curr_pos

    curr_pos += costs[0]  # increment the current position by the cost of reversing the first string

print(min_cost)  # print the minimum total cost
