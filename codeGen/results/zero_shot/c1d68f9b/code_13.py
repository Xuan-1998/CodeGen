import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

# Check if there are at least 3 knights and count the number of good and bad moods
if n < 3:
    print("NO")
elif sum(moods) % 2 != 0:
    print("YES" if max(set(moods), key=moods.count) == 1 else "NO")
else:
    print("YES" if len([i for i in moods if i == 1]) > 0 else "NO")
