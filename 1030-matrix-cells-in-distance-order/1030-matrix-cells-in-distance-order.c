int** allCellsDistOrder(int rows, int cols, int rCenter, int cCenter,
                        int* returnSize, int** returnColumnSizes) {
    int total = rows * cols;
    int** result = malloc(total * sizeof(int*));
    *returnColumnSizes = malloc(total * sizeof(int));
    int index = 0;

    for (int d = 0; d <= rows + cols; d++) {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (abs(r - rCenter) + abs(c - cCenter) == d) {
                    result[index] = malloc(2 * sizeof(int));
                    result[index][0] = r;
                    result[index][1] = c;
                    (*returnColumnSizes)[index] = 2;
                    index++;
                }
            }
        }
    }

    *returnSize = index;
    return result;
}