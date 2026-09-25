int compare(const void* a, const void* b) {
    return *(int*)b - *(int*)a;
}

int lastStoneWeight(int* stones, int stonesSize) {
    while (stonesSize > 1) {
        qsort(stones, stonesSize, sizeof(int), compare);

        if (stones[0] == stones[1]) {
            for (int i = 2; i < stonesSize; i++)
                stones[i - 2] = stones[i];

            stonesSize -= 2;
        } else {
            stones[0] = stones[0] - stones[1];

            for (int i = 2; i < stonesSize; i++)
                stones[i - 1] = stones[i];

            stonesSize--;
        }
    }

    return stonesSize == 0 ? 0 : stones[0];
}