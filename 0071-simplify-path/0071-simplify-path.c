#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/*
 Given a Unix-style absolute path, return its simplified canonical form.
 The caller is responsible for freeing the returned string.
*/
char* simplifyPath(const char* path) {
    if (!path) return NULL;

    // Duplicate the path to use with strtok (since it modifies the string)
    char *copy = strdup(path);
    if (!copy) return NULL;

    // Maximum tokens <= length of path
    int capacity = strlen(copy) + 1;
    char **stack = malloc(capacity * sizeof(char*));
    if (!stack) { free(copy); return NULL; }

    int top = 0;  // number of valid tokens in stack

    // Tokenize on slash '/', skipping empty segments
    for (char *token = strtok(copy, "/"); token != NULL; token = strtok(NULL, "/")) {
        if (strcmp(token, ".") == 0) {
            // no-op: current directory
        } else if (strcmp(token, "..") == 0) {
            // go one level up if possible
            if (top > 0) top--;
        } else {
            // ordinary directory name (e.g. "abc", "...", "_dir123")
            stack[top++] = token;
        }
    }

    char *result;
    if (top == 0) {
        result = strdup("/");  // only root remains
    } else {
        // Estimate total length: sum lengths + top (slashes) + 1 null
        size_t total_len = top + 1;
        for (int i = 0; i < top; ++i) {
            total_len += strlen(stack[i]);
        }
        result = malloc(total_len);
        if (!result) {
            free(copy);
            free(stack);
            return NULL;
        }

        char *ptr = result;
        *ptr++ = '/';
        for (int i = 0; i < top; ++i) {
            size_t len = strlen(stack[i]);
            memcpy(ptr, stack[i], len);
            ptr += len;
            if (i < top - 1) *ptr++ = '/';
        }
        *ptr = '\0';
    }

    free(copy);
    free(stack);
    return result;
}

/* Usage (outside submission):
#include <stdio.h>
int main(void) {
    const char *test[] = {
      "/home/", "/home//foo/", "/a/./b/../../c/", "/../", "/.../a/../b/c/../d/./"
    };
    for (int i = 0; i < 5; ++i) {
        char *ans = simplifyPath(test[i]);
        printf("Input: %s\nOutput: %s\n\n", test[i], ans);
        free(ans);
    }
    return 0;
}
*/

