import sys

def generate_subsets_and_sums(a):
    n = len(a)
    unique_sums = set()
    for i in range(2**n):
        subset_sum = 0
        for j in range(n):
            if (i & (1 << j)):
                subset_sum += a[j]
        unique_sums.add(subset_sum)
    return sorted(list(unique_sums))

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    print(" ".join(map(str, generate_subsets_and_sums(a))))
