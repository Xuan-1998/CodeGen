n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for subset in (tuple(arr[i:]for i in range(j+1))) for j in range(n)))
