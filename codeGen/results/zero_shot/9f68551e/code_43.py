def solve():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    # Sort the monsters by their appearance time
    sorted_k = sorted((k[i], i) for i in range(n))

    mana_used = 0

    for _, i in sorted_k:
        while mana_used < k[i]:
            mana_used += 1

        while mana_used >= h[i] and h[i] > 0:
            mana_used -= h[i]
            h[i] = 0

    print(mana_used)
