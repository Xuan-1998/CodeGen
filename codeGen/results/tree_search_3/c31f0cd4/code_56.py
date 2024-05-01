def find_all_sums(a):
    n = len(a)
    all_sums = set()
    for i in range(2**n):
        current_sum = 0
        for j in range(n):
            if ((i >> j) & 1):
                current_sum += a[j]
        all_sums.add(current_sum)
    return sorted(list(all_sums))

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(" ".join(map(str, find_all_sums(a))))
