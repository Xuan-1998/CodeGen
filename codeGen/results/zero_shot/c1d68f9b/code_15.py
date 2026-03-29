import sys
def solve():
    n = int(input())
    moods = list(map(int, input().split()))
    
    # Check if there are at least 3 knights
    if n < 3:
        print("NO")
        return
    
    # Find the number of good and bad moods
    good_mood_count = sum(moods)
    bad_mood_count = n - good_mood_count
    
    # Check if the number of good or bad moods is a multiple of (n-1)
    for i in range(2, int((n-1)**0.5) + 1):
        if (good_mood_count % i == 0 and good_mood_count // i <= n - 1) or \
           (bad_mood_count % i == 0 and bad_mood_count // i <= n - 1):
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
