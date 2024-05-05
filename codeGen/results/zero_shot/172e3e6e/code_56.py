def is_good_subsequence(subsequence):
    for i, num in enumerate(subsequence):
        if not num % (i + 1) == 0:
            return False
    return True

def count_good_subsequences(array):
    n = len(array)
    total_good_subsequences = 0
    for i in range(1, n + 1):  # consider subsequences of length from 1 to n
        for j in range(n - i + 1):  # consider starting positions
            subsequence = array[j:j+i]
            if is_good_subsequence(subsequence):
                total_good_subsequences += 1
    return total_good_subsequences % (10**9 + 7)

n = int(input())
array = list(map(int, input().split()))
print(count_good_subsequences(array))
