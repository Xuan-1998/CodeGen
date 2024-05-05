n = int(input())
p = list(map(int, input().split()))

def check_non_empty(p):
    return p[:n] and p[n:]

def find_mismatch(p):
    for i in range(n, len(p)):
        if p[i] <= p[:n][-1]:
            return True
    return False

def is_within_array(p):
    for i in range(n, len(p)):
        if p[i] <= p[:n][-1]:
            return True
    return False

result = "YES" if check_non_empty(p) and find_mismatch(p) and not is_within_array(p) else "NO"
print(result)
