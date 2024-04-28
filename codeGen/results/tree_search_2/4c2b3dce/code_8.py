from collections import defaultdict

def has_ab_and_ba():
    s = input()
    cache = defaultdict(bool)
    
    for i in range(len(s) - 1):
        if (s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A'):
            if not any(cache.values()):
                cache = {0: True, len(s) - 2: True}
            else:
                cache[0], cache[len(s) - 2] = True, True
        for j in range(i + 2, len(s)):
            if (s[i] == 'A' and s[j] == 'B') or (s[i] == 'B' and s[j] == 'A'):
                if not any(cache.values()):
                    cache[0], cache[j - 1] = True, True
                else:
                    cache[0], cache[j - 1] = True, True
    
    return "YES" if all(cache.values()) else "NO"


print(has_ab_and_ba())
