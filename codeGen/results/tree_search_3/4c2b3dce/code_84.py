import sys

def solve():
    s = input().strip()
    
    if len(s) < 2:
        print("NO")
        return
    
    dp = {(True, False): False, (False, True): False}  # Base cases
    ab_appears = ba_appears = False
    
    for c in s:
        if c == 'A':
            if not ab_appears and not ba_appears:
                dp[(c != 'B', not ab_appears or (ab_appears, ba_appears)[c == 'A'])] = not ab_appears
                if c == 'B' and not ab_appears:
                    ab_appears = True
            elif not dp[(c != 'B', (not ab_appears, ab_appears)[c == 'A'])]:
                print("NO")
                return
        else:
            if not ba_appears and not ab_appears:
                dp[(c != 'A', not ba_appears or (ab_appears, ba_appears)[c == 'B'])] = not ba_appears
                if c == 'A' and not ba_appears:
                    ba_appears = True
            elif not dp[(c != 'A', (not ba_appears, ba_appears)[c == 'B'])]:
                print("NO")
                return
    
    print("YES" if ab_appears or ba_appears else "NO")

if __name__ == "__main__":
    solve()
