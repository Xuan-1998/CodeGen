if __name__ == "__main__":
    import sys
    input = sys.stdin.read()
    stones = [int(x) for x in input.split()]
    print(can_cross_stones(stones))
