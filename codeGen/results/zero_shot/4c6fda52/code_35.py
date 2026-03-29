def min_changes():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        s = input()
        
        pref = [0] * (n + 1)
        prev = None
        for i, c in enumerate(s):
            if c != prev:
                pref[i+1] += 1
            prev = c
        
        print(max(pref) - k)

min_changes()
