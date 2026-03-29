import sys

def main():
    n = int(sys.stdin.readline().strip())

    def check_binary(n):
        binary = bin(n)[2:]
        count = 0
        prev_zero = True
        for bit in binary:
            if bit == '1':
                if prev_zero:
                    count += 1
                prev_zero = False
            else:
                prev_zero = True
        return count

    result = sum(1 for i in range(n+1) if check_binary(i))
    print(result)

if __name__ == "__main__":
    main()
