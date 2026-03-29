import sys

def main():
    root = [int(x) for x in next(sys.stdin).split()]
    result = max_path_sum(root)
    print(result)

if __name__ == "__main__":
    main()
