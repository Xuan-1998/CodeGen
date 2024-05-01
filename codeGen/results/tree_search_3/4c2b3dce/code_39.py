import sys
from collections import defaultdict

def main():
    s = input()
    found_AB = defaultdict(bool)
    found_BA = defaultdict(bool)

    for i in range(len(s)):
        if i >= 2 and s[i-2:i] == 'AB':
            found_AB[i] = True
        if i >= 1 and s[i-1:i+1] == 'BA' and not any(found_AB[j] for j in range(i)):
            found_BA[i] = True

    print("YES" if found_AB[len(s)-2] and found_BA[0] else "NO")

if __name__ == "__main__":
    main()
