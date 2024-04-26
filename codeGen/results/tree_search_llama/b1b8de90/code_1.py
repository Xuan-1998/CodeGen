def recursive_sort(permutation, x):
    if x == 0 or permutation[x-1] <= permutation[x]:
        return permutation
    else:
        permutation[x-1], permutation[x] = permutation[x], permutation[x-1]
        return recursive_sort(permutation, x-1)

n = int(input())  # read input from stdin

permutation = list(range(1, n+1))  # initialize the permutation with integers from 1 to n
x = len(permutation) - 1  # start with the last element

sorted_permutation = recursive_sort(permutation[:], x)
print(' '.join(map(str, sorted_permutation)))  # print the sorted permutation as a single line of space-separated integers
