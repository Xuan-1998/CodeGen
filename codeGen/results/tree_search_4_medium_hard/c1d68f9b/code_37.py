def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))

    memo = {}

    def is_good_mood(knight_index):
        good_mood_knights = sum(moods[:knight_index])
        return (good_mood_knights % 2) == 0

    for i in range(n):
        if not is_good_mood(i):
            continue
        memo[(i, moods[i])] = "YES"
        for j in range(i + 1, n):
            if is_good_mood(j):
                if (j, moods[j]) not in memo:
                    memo[(j, moods[j])] = "NO"
                else:
                    memo[(j, moods[j])] = "YES"

    return "YES" if any(val == "YES" for val in memo.values()) else "NO"


print(can_form_polygon())
