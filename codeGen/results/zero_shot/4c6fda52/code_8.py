def min_changes(n, k, s):
    # Count mismatches in the first k-1 characters
    mismatches = sum(c1 != c2 for c1, c2 in zip(s[:k-1], "RGB"*((k-1)//3)))
    
    # Add mismatch between last characters
    mismatches += 0 if s[-1] == "RGB"[k%3] else 1
    
    return mismatches

n = int(input())
for _ in range(n):
    k = int(input())
    s = input()
    print(min_changes(k, n, s))
