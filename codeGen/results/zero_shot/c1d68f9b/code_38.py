from sys import stdin

def solve():
    n = int(stdin.readline())
    moods = list(map(int, stdin.readline().split()))
    
    good_count = sum(moods)
    bad_count = n - good_count
    
    if good_count == 0 or bad_count == 0:
        print("NO")
    else:
        for i in range(1, len(moods)):
            if moods[i] != moods[0]:
                break
        else:
            print("YES")
        return

if __name__ == "__main__":
    solve()
