import sys
n = int(sys.stdin.readline())
mood = list(map(int, sys.stdin.readline().split()))
can_form = True
for i in range(len(mood) - 1):
    if mood[i] == 0 and mood[i + 1] == 0:
        can_form = False
        break

print("YES" if can_form else "NO")
