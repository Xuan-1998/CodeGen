def min_changes(s, k):
    if len(s) < k:
        return 0
    
    changes = 0
    for i in range(len(s)-k+1):
        if s[i:i+k] != "RGB":
            changes += k - (s[i:i+k].count("R") + s[i:i+k].count("G") + s[i:i+k].count("B"))
    
    return changes

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    
    s = input()
    print(min_changes(s, k))
