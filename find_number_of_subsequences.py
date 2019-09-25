"""
Task:
Given two strings A and B,
find the number of times
the second string occurs in the first string,
whether continuous or discontinuous.
"""


def number_of_subsequences(size_A, size_B, A, B):
    if size_A == 0:
        return 0

    if size_B == 0:
        return 1

    dp = [[0] * size_A for _ in range(size_B)]

    for i in range(size_B):
        for j in range(i, size_A):
            if i == 0:
                if j == 0:
                    dp[i][j] = 1 if A[j] == B[i] else 0
                else:
                    dp[i][j] = dp[i][j - 1] + 1 if A[j] == B[i] else dp[i][j - 1]
            else:
                if A[j] != B[i]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    return dp[size_B - 1][size_A - 1]


if __name__ == '__main__':
    for _ in range(int(input())):
        size_A, size_B = [int(num) for num in input().split()]
        A, B = [string for string in input().split()]
        print(number_of_subsequences(size_A, size_B, A, B))
