bool canThreePartsEqualSum(int* arr, int arrSize) {
    int sum = 0;

    for (int i = 0; i < arrSize; i++)
        sum += arr[i];

    if (sum % 3 != 0)
        return false;

    int target = sum / 3;
    int count = 0;
    int current = 0;

    for (int i = 0; i < arrSize; i++) {
        current += arr[i];

        if (current == target) {
            count++;
            current = 0;
        }
    }

    return count >= 3;
}