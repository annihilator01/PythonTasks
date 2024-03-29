"""
Task:
Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number S.
"""


for _ in range(int(input())):
    n, subarray_sum = [int(num) for num in input().split()]

    array_sum = [0]
    for num in input().split():
        array_sum.append(array_sum[len(array_sum) - 1] + int(num))

    left = right = 0

    while right < len(array_sum) and array_sum[right] - array_sum[left] != subarray_sum:
        if array_sum[right] - array_sum[left] < subarray_sum:
            right += 1
        elif array_sum[right] - array_sum[left] > subarray_sum:
            left += 1

    print(left + 1, right) if right < len(array_sum) else print(-1)
