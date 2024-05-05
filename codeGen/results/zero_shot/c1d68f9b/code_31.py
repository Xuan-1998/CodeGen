import sys
n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))
if any(mood == 1 and (i+1<n and moods[i+1] == 1) for i in range(n)):
    print("YES")
else:
    print("NO")
