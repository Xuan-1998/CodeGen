n, k = map(int, input().split())
s = input()

changes_needed_in_s = 0
changes_needed_in_infinite_string = 0

if s[:k] != s[k:k*2]:
    changes_needed_in_s += k
    changes_needed_in_infinite_string = k
elif s[-k:] != s[k*k-1:k*2]:
    changes_needed_in_s += k
    changes_needed_in_infinite_string = k
else:
    count = 0
    for i in range(n-k+1):
        if s[i:i+k] == s[:k]:
            count += 1
    if count < n//k + 1:
        changes_needed_in_s = (n - count*k)

print(min(changes_needed_in_s, changes_needed_in_infinite_string))
