#include <stdio.h>
#include <stdlib.h>

int largestRectangleArea(int* heights, int heightsSize) {
    if (heightsSize == 0) return 0;
    
    int* left = (int*)malloc(heightsSize * sizeof(int));
    int* right = (int*)malloc(heightsSize * sizeof(int));
    int* stack = (int*)malloc(heightsSize * sizeof(int));
    int top = -1;
    
    // Fill left boundaries
    for (int i = 0; i < heightsSize; i++) {
        while (top >= 0 && heights[stack[top]] >= heights[i]) {
            top--;
        }
        if (top < 0) {
            left[i] = 0;
        } else {
            left[i] = stack[top] + 1;
        }
        stack[++top] = i;
    }
    
    top = -1;
    // Fill right boundaries
    for (int i = heightsSize - 1; i >= 0; i--) {
        while (top >= 0 && heights[stack[top]] >= heights[i]) {
            top--;
        }
        if (top < 0) {
            right[i] = heightsSize - 1;
        } else {
            right[i] = stack[top] - 1;
        }
        stack[++top] = i;
    }
    
    int max_area = 0;
    for (int i = 0; i < heightsSize; i++) {
        int area = heights[i] * (right[i] - left[i] + 1);
        if (area > max_area) {
            max_area = area;
        }
    }
    
    free(left);
    free(right);
    free(stack);
    return max_area;
}