n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(any(sum(i) % m == 0 for i in (pow(2, j)*sum(arr[i-j//2:i]) for j in range(n+1))))
