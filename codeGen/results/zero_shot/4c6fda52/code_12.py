def min_changes(s, k):
    n = len(s)
    changes = 0
    
    for i in range(n - k + 1):
        pattern = s[i:i+k]
        
        if pattern[0] != 'R' or pattern[1] != 'G' or pattern[2] != 'B':
            continue
        
        for j in range(i, n, k):
            if s[j:j+k] != pattern:
                changes += 1
                break
    
    return changes

def main():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        
        print(min_changes(s, k))

if __name__ == "__main__":
    main()
