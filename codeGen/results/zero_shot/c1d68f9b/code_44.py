n = int(input())
moods = list(map(int, input().split()))
if sum(moods) % 2 != 0:
    print("YES")
else:
    print("NO")
