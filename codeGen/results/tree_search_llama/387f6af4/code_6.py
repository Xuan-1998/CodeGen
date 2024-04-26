def find_complement(N):
    # Convert the integer to binary, remove the '0b' prefix, and count the number of bits
    bin_N = bin(N)[2:]
    num_bits = len(bin_N)

    # Calculate the complement by flipping each bit (1s become 0s and vice versa)
    complement = int('1' * num_bits - bin_N, 2)

    return complement

def main():
    N = int(input())
    print(find_complement(N))

if __name__ == "__main__":
    main()
