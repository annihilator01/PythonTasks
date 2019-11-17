"""
Task:
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        h, h_inv = self.polynomial_hash(s)

        l_odd, r_odd = self.max_palindrome(s, h, h_inv, 1)
        l_even, r_even = self.max_palindrome(s, h, h_inv, 0)

        if (r_odd - l_odd) > (r_even - l_even):
            return s[l_odd:r_odd + 1]
        else:
            return s[l_even:r_even + 1]

    def polynomial_hash(self, s):
        p = 31
        self.m = int(1e9 + 9)
        self.p_pow = [(p**i) % self.m for i in range(len(s))]
        h = [0] * (len(s) + 1)
        h_inv = [0] * (len(s) + 1)

        for i in range(len(s)):
            h[i + 1] = (h[i] + (ord(s[i]) - ord('a') + 1) * self.p_pow[i]) % self.m
            h_inv[i + 1] = (h_inv[i] + (ord(s[len(s) - i - 1]) - ord('a') + 1) * self.p_pow[i]) % self.m
        return h, h_inv

    def binary_search(self, s, h, h_inv, l, r, k):
        left = l
        right = r
        r_2 = r + k + 1
        mx_plm = (0, 0)

        while right >= left:
            mid = (left + right) // 2
            mid_2 = 2 * r - mid + k + 1
            left_hash = (h[r + 1] - h[mid]) % self.m
            right_hash = (h_inv[len(s) - r_2] - h_inv[len(s) - mid_2 - 1]) % self.m

            if len(s) - mid_2 - 1 > mid:
                left_hash = (left_hash * self.p_pow[len(s) - mid_2 - 1 - mid]) % self.m
            else:
                right_hash = (right_hash * self.p_pow[mid - (len(s) - mid_2 - 1)]) % self.m

            if left_hash == right_hash:
                mx_plm = (mid, mid_2) if mid_2 - mid > mx_plm[1] - mx_plm[0] else mx_plm
                right = mid - 1
            else:
                left = mid + 1

        return mx_plm

    def max_palindrome(self, s, h, h_inv, k):
        mx_plm = (0, 0)

        for i in range(k, len(s) - 1):
            if i < len(s) - i + k - 2:
                left_border = 0
            else:
                left_border = i - (len(s) - i + k - 2)

            new_plm = self.binary_search(s, h, h_inv, left_border, i - k, k)
            mx_plm = new_plm if new_plm[1] - new_plm[0] > mx_plm[1] - mx_plm[0] else mx_plm

        return mx_plm


if __name__ == '__main__':
    solution = Solution()
    s = 'babad'
    print(solution.longestPalindrome(s))
