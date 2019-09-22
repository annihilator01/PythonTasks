def find_max_index_dif(n, array):
    min_before = [0] * n
    max_after = [0] * n

    min_before[0] = array[0]
    for i in range(1, n):
        min_before[i] = min(min_before[i - 1], array[i])

    max_after[n - 1] = array[n - 1]
    for j in range(n - 2, -1, -1):
        max_after[j] = max(max_after[j + 1], array[j])

    i, j = 0, 0
    max_diff = -1
    while i < n and j < n:
        if max_after[j] >= min_before[i]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1

    return max_diff


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        array = [int(num) for num in input().split()]
        print(find_max_index_dif(n, array))
