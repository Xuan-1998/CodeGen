def is_good_subsequence(subsequence):
    for i in range(1, len(subsequence) + 1):
        if subsequence[i - 1] % i != 0:
            return False
    return True

def get_subsequences(array, index, subsequence):
    if index == len(array):
        yield tuple(subsequence)
    else:
        for i in range(index, len(array)):
            subsequence.append(array[i])
            yield from get_subsequences(array, i + 1, subsequence)
            subsequence.pop()

n = int(input())
a = [int(x) for x in input().split()]

good_subsequences = (subsequence for subsequence in get_subsequences(a, 0, []) if is_good_subsequence(subsequence))
num_good_subsequences = sum(1 for _ in good_subsequences) % (10**9 + 7)
print(num_good_subsequences)
