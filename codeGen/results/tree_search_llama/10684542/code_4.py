def getExponent(n, p):
    # Create a binary tree to store powers of p
    root = Node(p ** 0)

    for i in range(1, int(math.log2(n)) + 1):
        power = p ** i
        if n % power == 0:
            node = Node(power)
            current = root
            while True:
                prev_power = current.value
                if n % prev_power > 0:
                    current.right = node
                    break
                elif n % prev_power < 0:
                    current.left = node
                    break
                else:
                    current = node
        else:
            # If p^i is not divisible by n, move to the right subtree
            current = root
            while True:
                prev_power = current.value
                if n % prev_power > 0:
                    current.right = Node(p ** (i + 1))
                    break
                elif n % prev_power < 0:
                    current.left = Node(p ** (i - 1))
                    break

    # Find the largest exponent x such that p^x evenly divides n
    max_exponent = 0
    node = root
    while True:
        if node.right is None:
            return max_exponent
        else:
            max_exponent += 1
            node = node.right

def Node(value):
    self.value = value
    self.left = None
    self.right = None
