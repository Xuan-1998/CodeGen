a = [int(x) for x in input().split()]
n = len(a)
def generate_subsequences(a, n):
    if n == 0:
        return [([], 1)]
    subs = []
    for i in range(n + 1):
        prev_subs = generate_subsequences(a, i - 1)
        for sub, _ in prev_subs:
            subs.append((sub + (a[i],), sub[0] if len(sub) == 0 else (sub[-1] % a[i]) == 0))
    return subs
def is_good_subsequence(sub):
    for i in range(1, len(sub)):
        if (sub[i] % i) != 0:
            return False
    return True

goodsubs = []
for sub, _ in generate_subsequences(a, n - 1):
    if is_good_subsequence(sub):
        goodsubs.append(sub)
count = 0
for sub in goodsubs:
    count += 1
print(count % (10 ** 9 + 7))
