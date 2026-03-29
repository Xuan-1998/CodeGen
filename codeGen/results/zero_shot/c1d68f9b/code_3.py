n = int(input())
moods = list(map(int, input().split()))

# Check if there are at least 3 knights
if n < 3:
    print("NO")
else:
    for i in range(1, n-1):
        if (moods[i] == 0 and moods[(i-1)%n] == 0) or (moods[i] == 0 and moods[(i+1)%n] == 0):
            print("NO")
            break
    else:
        print("YES")
