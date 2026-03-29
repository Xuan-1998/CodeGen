def count_good_subsequences(n, a):
    MOD = 10**9 + 7
    good_subsequences = 0

    for i in range(1, n+1):
        valid_numbers = [x for x in a if x % i == 0]
        subsequence_count = 1
        for j in range(i-1, -1, -1):
            subsequence_count *= j
            subsequence_count %= MOD

        good_subsequences += len(valid_numbers) * subsequence_count
        good_subsequences %= MOD

    return good_subsequences

n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(n, a))
