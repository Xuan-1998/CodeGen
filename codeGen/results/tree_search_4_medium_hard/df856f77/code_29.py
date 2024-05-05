from bisect import insort

N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

for i in range(1, N):
    if A[i] > lis[-1]:
        lis.append(A[i])
    else:
        idx = bisect.bisect_left(lis, A[i])
        lis[idx] = A[i]

dp = len(A) - len(lis)
print(dp)
