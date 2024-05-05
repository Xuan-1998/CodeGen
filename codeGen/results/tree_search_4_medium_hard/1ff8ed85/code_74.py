def send_sequence_b(a):
    n = len(a)
    b_sum = sum(b)

    if sum([i * (n - i) for i in range(1, n)]) != b_sum:
        return "NO"

    res = []
    for i in range(n):
        j = 0
        while a[i] > b[j]:
            if j == n - 1:
                return "NO"
            j += 1

        while a[i] >= b[j]:
            res.append(a[i])
            j += 1

    if sum(res) != b_sum:
        return "NO"

    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        print(send_sequence_b(b))


if __name__ == "__main__":
    main()
