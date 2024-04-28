n = int(input())
m = int(input())
numbers = list(map(int, input().split()))

def find_subset_sum_divisible_by_m():
    for i in range(1 << n):
        subset_sum = 0
        for j in range(n):
            if (i & (1 << j)):
                subset_sum += numbers[j]
        if subset_sum % m == 0:
            return 1
    return 0

print(find_subset_sum_divisible_by_m())
