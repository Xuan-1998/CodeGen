import math

def read_input():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A, B = map(int, input().split()), map(int, input().split())
        yield A, B

def calculate_carry(A, B):
    carry_count = 0
    for a, b in zip(map(str, A), map(str, B)):
        if len(a) > 1 or len(b) > 1:
            return 10**len(max((a, b), key=len)) - 1
        c = str(int(a) + int(b))
        carry_count += (c[0] == '1')
    return carry_count

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        expected_carry = sum(calculate_carry(A, B) / math.comb(N, 2) for A, B in read_input()) / T
        print(f"{expected_carry:.9f}")

if __name__ == "__main__":
    main()
