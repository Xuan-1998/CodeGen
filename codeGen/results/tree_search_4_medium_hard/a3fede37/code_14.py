def maxPathSum(tree, n):
    dp = [-1] * n

    def maxPathSumUtil(node):
        if node >= n or not hasLeftChild(node) and not hasRightChild(node):
            return tree[node]
        
        leftSum = 0 if not hasLeftChild(node) else maxPathSumUtil(leftChild(node))
        rightSum = 0 if not hasRightChild(node) else maxPathSumUtil(rightChild(node))

        dp[node] = tree[node] + max(leftSum, rightSum)

        return dp[node]

    for i in range(n):
        maxPathSumUtil(i)
    
    return max(max(dp), default=-1)

# Sample implementation of the hasLeftChild and hasRightChild functions
def hasLeftChild(node):
    # implement your logic here
    pass

def leftChild(node):
    # implement your logic here
    pass

def rightChild(node):
    # implement your logic here
    pass
