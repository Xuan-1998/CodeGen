import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if n < 3:
    print("NO")
else:
    good_mood_count = sum(moods)
    
    if (good_mood_count % 2) == 1:  # odd number of "good mood" knights
        print("YES" if good_mood_count > 0 else "NO")
    else:  # even number of "good mood" knights
        alternating = all(moods[i] != moods[(i+1)%n] for i in range(n))
        print("YES" if (good_mood_count > 0 and alternating) or (good_mood_count == 0 and n % 2 == 1) else "NO")
