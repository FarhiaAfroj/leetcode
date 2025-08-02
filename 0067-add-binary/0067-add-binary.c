#include <stdlib.h>
#include <string.h>

char* addBinary(char* a, char* b) {
    int lenA = strlen(a), lenB = strlen(b);
    int maxLen = lenA > lenB ? lenA : lenB;
    // Allocate one extra for possible carry + null terminator
    char* res = malloc(maxLen + 2);
    if (!res) return NULL;

    res[maxLen + 1] = '\0';

    int carry = 0;
    int i = lenA - 1, j = lenB - 1, k = maxLen;

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) {
            sum += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            sum += b[j] - '0';
            j--;
        }
        res[k] = (char)((sum % 2) + '0');
        carry = sum / 2;
        k--;
    }

    // If no carry remains, k >= 0; shift string right so res points to the first '1'
    if (k >= 0) {
        int start = k + 1;
        // Total chars from start (including null) = (maxLen + 1) - start + 1
        memmove(res, res + start, (maxLen + 1) - start + 1);
    }

    return res;
}
