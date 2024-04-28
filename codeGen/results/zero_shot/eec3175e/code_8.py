n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for subset in ([],] + (combinations(arr, i) for i in range(len(arr)+1)))))
