n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    subsegment = arr[l-1:r]
    if all(subsegment[i] <= subsegment[i+1] for i in range(len(subsegment)-1)) and \
       all(subsegment[i] >= subsegment[i+1] for i in range(1, len(subsegment))):
        print("Yes")
    else:
        print("No")
