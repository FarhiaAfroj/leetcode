#include <string.h>  // for strlen()

/**
 * Computes the minimum number of operations (insert/delete/replace)
 * to transform word1 into word2.
 *
 * LeetCode's driver provides word1 and word2 as char pointers,
 * so this exact function name and signature must be submitted.
 */
int minDistance(char *word1, char *word2) {
    int m = strlen(word1);
    int n = strlen(word2);

    // Allocate a (m+1) × (n+1) DP table
    int dp[m + 1][n + 1];

    for (int i = 0; i <= m; i++) dp[i][0] = i;  // deletes
    for (int j = 0; j <= n; j++) dp[0][j] = j;  // inserts

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];  // no change
            } else {
                int ins = dp[i][j - 1] + 1;
                int del = dp[i - 1][j] + 1;
                int rep = dp[i - 1][j - 1] + 1;
                dp[i][j] = (ins < del ? (ins < rep ? ins : rep)
                                     : (del < rep ? del : rep));
            }
        }
    }

    return dp[m][n];
}

