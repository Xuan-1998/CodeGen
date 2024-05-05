import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

n_good_mood = sum(moods)

if n_good_mood < 3:
    print("NO")
else:
    for _ in range(n):
        swapped = False
        for i in range(len(moods)):
            if moods[i] == 0:
                good_mood_idx = (i + 1) % len(moods)
                while moods[good_mood_idx] == 0:
                    good_mood_idx = (good_mood_idx + 1) % len(moods)
                moods[i], moods[good_mood_idx] = moods[good_mood_idx], moods[i]
                swapped = True
                break
        if not swapped:
            print("YES")
            sys.exit(0)

print("NO")
