n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(any(sum(temps) % m == 0 for temps in ((arr[i],) + temps for i, temps in enumerate(arr))))
