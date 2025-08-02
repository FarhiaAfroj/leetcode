#include <string.h>
#include <ctype.h>

int lengthOfLastWord(char *s) {
    int i = strlen(s) - 1;
    // Skip trailing spaces
    while (i >= 0 && isspace((unsigned char)s[i])) {
        i--;
    }
    // Count characters of the last word
    int count = 0;
    while (i >= 0 && !isspace((unsigned char)s[i])) {
        count++;
        i--;
    }
    return count;
}
