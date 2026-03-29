First, let's understand the problem better. We are given a sequence of non-negative integers d, which represents the out-degree of each vertex in a directed tree. We need to find the sum of the numbers of good vertices for all good trees.

A good tree is a tree that satisfies the following conditions:
1. The out-degree of vertex i is d_i.
2. A vertex v is called a good vertex if the minimum vertex number in the subtree rooted at v is v.

To solve this problem, we can use dynamic programming. Here are the steps:

1. Initialize an array dp of size N+1, where dp[i] is the number of good vertices in the subtree rooted at vertex i.
2. Initialize an array prefix of size N+1 to store the prefix sum of dp. prefix[i] is the sum of dp[j] for all 0<=j<=i.
3. Iterate over the sequence d from the end to the beginning. For each vertex i, calculate dp[i] = dp[i+1]*d[i] + prefix[i+d[i]] - prefix[i]. This is because each child of vertex i can be a good vertex, and each vertex in the subtree rooted at vertex i+d[i] can be a good vertex.
4. The answer is the sum of all dp[i] modulo 998244353.

Let's implement this in Python.
