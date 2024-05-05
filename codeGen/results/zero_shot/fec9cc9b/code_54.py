n, m = map(int, input().split())
array = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    subsegment = array[l-1:r]
    decreasing = all(subsegment[i] >= subsegment[i+1] for i in range(len(subsegment)-1))
    increasing = all(subsegment[i] <= subsegment[i+1] for i in range(len(subsegment)-1))
    if decreasing and increasing:
        print("Yes")
    else:
        print("No")
