import sys

ab_before_ba = False
found_ab_or_ba = False

for char in sys.stdin.readline():
    if char == 'A' and not ab_before_ba:
        ab_before_ba = True
    elif char == 'B':
        if not found_ab_or_ba:
            found_ab_or_ba = True
        else:
            if ab_before_ba:
                print("YES")
                sys.exit(0)
            else:
                print("NO")
                sys.exit(0)

print("NO" if not found_ab_or_ba else "YES")
