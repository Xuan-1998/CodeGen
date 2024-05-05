def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def preprocess_permutation(p):
    n = len(p) // 2
    left = p[:n]
    right = p[n:]
    return left, right

def check_merge(left, right):
    if len(left) == 0:
        return merge(right, [])
    if len(right) == 0:
        return merge(left, [])

    left_head = left[0]
    right_head = right[0]

    if left_head <= right_head:
        merged = merge(left[1:], right)
    else:
        merged = merge(left, right[1:])

    return merged == p

def solve(p):
    left, right = preprocess_permutation(p)
    result = check_merge(left, right)
    return "YES" if result else "NO"

import sys
input_file = open('in.txt', 'r')
n = int(input_file.readline())
p = list(map(int, input_file.readline().split()))
sys.stdout.write(str(solve(p)) + '\n')

