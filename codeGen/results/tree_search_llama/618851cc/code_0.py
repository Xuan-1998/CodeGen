from typing import Set

def find_pair(a: Set[int], b: Set[int]) -> tuple:
    for a_val in a:
        for b_val in b:
            if (a_val + b_val) not in a and (a_val + b_val) not in b:
                return (a_val, b_val)
    return None

if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))

    pair = find_pair(A, B)

    if pair:
        print(*pair)
    else:
        print("No such pair exists")
