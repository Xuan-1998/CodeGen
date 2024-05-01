def solve():
    s = input()
    
    found_ab = False
    found_ba = False
    
    for i, c in enumerate(s):
        if i >= 1:
            prev_c = s[i-1]
            if (c == 'A' and prev_c == 'B') or (c == 'B' and prev_c == 'A'):
                if not found_ab:
                    found_ab = True
                elif not found_ba:
                    found_ba = True
    
    print('YES' if found_ab and found_ba else 'NO')

if __name__ == "__main__":
    solve()
