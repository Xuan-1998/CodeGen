n = int(input())
m = int(input())
nums = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for subset in ([],] + combinations(nums, i+1)) for i in range(n)))
