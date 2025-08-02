// Return the number of ways to climb 'n' stairs (n ≥ 1).
// Constraints: 1 ≤ n ≤ 45
int climbStairs(int n) {
    if (n == 1) return 1;  // Only one way: take one step.

    // Let prev2 = ways to reach step (i-2), prev1 = ways to reach step (i-1)
    int prev2 = 1;  // ways(1st step) = 1
    int prev1 = 2;  // ways(2nd step) = 2

    // From i = 3 to n, build up by summing the previous two
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
