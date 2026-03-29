def count_changes(s, k):
    changes = 0
    
    for i in range(len(s) - k + 1):
        if s[i:i+k] == (s[i] * k):
            break
        changes += 1
    
    return changes

def main():
    while True:
        n, k = map(int, input().split())
        if not (n <= 2 * 10**5 and k <= n):
            break
        
        s = input()
        
        changes = count_changes(s, k)
        print(changes)

if __name__ == "__main__":
    main()
