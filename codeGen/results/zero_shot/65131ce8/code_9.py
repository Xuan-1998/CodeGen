To solve this problem, we can use dynamic programming. The main idea is to keep track of the number of good vertices for all subtrees of the tree. 

Here are the steps to solve this problem:

1. First, we need to calculate the prefix and suffix sums of the degrees. For this, we can create two lists, prefix and suffix, where prefix[i] is the sum of the first i degrees and suffix[i] is the sum of the last i degrees.

2. Next, we initialize a 2D DP table dp[i][j] where dp[i][j] represents the number of good trees with i vertices and j good vertices. Initially, all values in dp are set to 0. 

3. The base case for the DP table is dp[0][0] = 1, which represents the situation where there are no vertices and hence no good vertices.

4. We then fill up the DP table using the following transition: for each i from 1 to N and for each j from 0 to i, we update dp[i][j] by adding dp[prefix[i-1]][k] * dp[suffix[N-i]][j-k] for all k from 0 to j. This represents the situation where we split the i vertices into two subtrees, one with prefix[i-1] vertices and the other with suffix[N-i] vertices, and distribute the j good vertices among these two subtrees.

5. Finally, the answer to the problem is the sum of dp[N][j] for all j from 0 to N, modulo 998244353.

Let's implement this in Python.
