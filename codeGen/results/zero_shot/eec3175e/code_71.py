n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(any(sum(subset) % m == 0 for subset in (tuple(arr[i:]for i in range(r+1))), r=range(len(arr))))
