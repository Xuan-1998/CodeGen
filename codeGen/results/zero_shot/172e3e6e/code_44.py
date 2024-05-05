def is_good_subsequence(subseq):
    n = len(subseq)
    for i in range(1, n+1):
        if subseq[i-1] % i != 0:
            return False
    return True

def count_good_subsequences(a):
    n = len(a)
    total_subsequences = 2**n - 1  # number of non-empty subsequences
    good_subsequences = 0
    for i in range(1, total_subsequences+1):  # iterate over all non-empty subsequences
        subseq = [a[j] for j in range(n) if (i & (1 << j))]
        if is_good_subsequence(subseq):
            good_subsequences += 1
    return good_subsequences % (10**9 + 7)

n = int(input())  # read the length of the array
a = [int(x) for x in input().split()]  # read the array

result = count_good_subsequences(a)
print(result)
