import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))

        # Sort the monsters by their appearance times
        sorted_k = sorted((k_i, h_i) for k_i, h_i in zip(k, h))

        # Initialize the minimum mana required
        min_mana = 0

        # Iterate over the sorted monsters
        for _, h_i in sorted_k:
            # Update the minimum mana required to kill this monster
            while min_mana < h_i - 1:
                min_mana += 1
            min_mana += h_i

        print(min_mana)

if __name__ == '__main__':
    main()
