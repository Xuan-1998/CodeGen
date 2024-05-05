def get_subsequences(a):
    def generate_subsequences(index, sequence):
        if index >= len(a):
            return [sequence]
        subsequences = []
        for i in range(index, len(a)):
            subsequences.extend(generate_subsequences(i + 1, sequence + [a[i]]))
        return subsequences
    return generate_subsequences(0, [])

def is_good_subsequence(subsequence):
    for i in range(1, len(subsequence) + 1):
        if subsequence[i - 1] % i != 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(a))

def count_good_subsequences(a):
    subsequences = get_subsequences(a)
    return sum(1 for subsequence in subsequences if is_good_subsequence(subsequence)) % (10**9 + 7)
