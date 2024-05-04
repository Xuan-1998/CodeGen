def count_blocks(n):
    mod = 998244353
    counts = [0] * (n + 1)
    for i in range(10**n):
        s = str(i).zfill(n)
        length = len(set(s))
        counts[length] += 1
    return " ".join(str(counts[i]) for i in range(n)) + "\n"

if __name__ == "__main__":
    n = int(input())
    print(count_blocks(n))
