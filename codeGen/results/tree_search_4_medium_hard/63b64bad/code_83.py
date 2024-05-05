def simulate_program(sequence):
    n = len(sequence)
    dp = {}

    for y in range(n):
        for x in range(2, n+1):
            a_x = sequence[x-1]
            if x > 1:
                new_y = y + a_x - sequence[x-1]
                dp[(y, a_x)] = dp.get((new_y, a_x), new_y)
            else:
                dp[(y, a_x)] = y + a_x

    for i in range(2, n+1):
        t = dp.get((i-1, sequence[i-1]), -1)
        if t <= 0 or t > n:
            return -1
        y += sequence[i-1]
        x = (x + sequence[i-1]) % (n+1)

    return y

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    for i in range(n-1):
        print(simulate_program(sequence))
        sequence = [0]  # Reset the sequence for the next iteration

if __name__ == "__main__":
    main()
