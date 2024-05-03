if __name__ == "__main__":
    import sys
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    max_distance = find_max_distance(commands, n)
    print(max_distance)
