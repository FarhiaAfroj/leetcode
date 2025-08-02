#include <stdint.h>

// Return the floor of the square root of x (0 ≤ x ≤ 2³¹−1)
int mySqrt(int x) {
    if (x <= 1)     // √0 = 0; √1 = 1
        return x;

    int left = 0, right = x;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        // Compare without overflow: check mid ≤ x / mid instead of mid * mid ≤ x
        if (mid <= x / mid) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    // At loop exit, right = the largest integer whose square ≤ x
    return right;
}
