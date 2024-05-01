import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(' '.join(map(str, winning_teams(n, s))))

if __name__ == '__main__':
    main()
