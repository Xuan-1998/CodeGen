code
x = 0
a_xor_y = a
for i in range(b.bit_length()):
    if (y >> i) & 1:
        x |= 1 << i
    else:
        x &= ~(1 << i)
print(x, a - x)
