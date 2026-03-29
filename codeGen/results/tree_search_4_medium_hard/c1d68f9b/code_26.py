dp = {}

def solve(n, moods):
    if (n, tuple(moods)) in dp:
        return dp[(n, tuple(moods))]
    
    if n < 3:
        return "NO"
    
    for i in range(n):
        if moods[i] == 1:  # good mood
            remaining_moods = moods[:i] + moods[i+1:]
            required_good_moods = (n + 1) // 2
            if sum(remaining_moods[:required_good_moods]) >= required_good_moods:
                dp[(n, tuple(moods))] = "YES"
                return "YES"
    
    dp[(n, tuple(moods))] = "NO"
    return "NO"

def main():
    n = int(input())
    moods = list(map(int, input().split()))
    print(solve(n, moods))

if __name__ == "__main__":
    main()
