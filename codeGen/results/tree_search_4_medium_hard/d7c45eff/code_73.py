import sys

# Read input
n, k = map(int, input().split())
s = input()

dp = {}
def get_smallest(s, duplication):
    if (s, duplication) in dp:
        return dp[(s, duplication)]
    
    if len(s) > k:
        return ''
    
    if len(s) == k:
        return s
    
    result = None
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if not duplication and (t, False) in dp and (s, False) in dp:
            result = min((dp[(s, False)], dp[(t, False)]), key=lambda x: (-ord(x[0]), -x[1]))
        elif duplication and (s[:i], True) in dp and (t, False) in dp:
            result = min((dp[(s[:i], True)], dp[(t, False)]), key=lambda x: (-ord(x[0]), -x[1]))
        if result is None:
            continue
        return result
    if duplication:
        t = s + s
        if (t, True) in dp:
            return (dp[(t, True)],)
        else:
            return ('', )
    return ('', )

smallest_str = get_smallest(s, False)
print(''.join(smallest_str))
