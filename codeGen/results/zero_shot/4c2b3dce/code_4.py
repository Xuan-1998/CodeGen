import sys
s = sys.stdin.readline().strip()
if "AB" in s or "BA" in s:
    rem_s = s.replace("AB", "").replace("BA", "")
    if len(rem_s) == 0 or ("AB" not in rem_s and "BA" not in rem_s):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
