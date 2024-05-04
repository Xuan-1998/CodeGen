import sys

n = int(sys.stdin.readline())

integers = generate_integers(n)
block_counts = count_blocks(integers)
modulo_counts = calc_modulo(block_counts)

print_output(modulo_counts)
