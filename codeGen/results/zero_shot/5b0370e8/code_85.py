import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_xor_count = 0
        for i in range(2**k):
            and_xor_value = 0
            xor_value = 0
            array = []
            for j in range(k):
                if (i >> j) & 1:
                    array.append(i)
            for num in array:
                and_xor_value |= num
                xor_value ^= num
            if and_xor_value >= xor_value:
                and_xor_count += 1
        print(and_xor_count % (10**9 + 7))

if __name__ == "__main__":
    solve()
