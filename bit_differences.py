"""
Task:
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed
from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in
binary representations of x and y.
For example, bit difference for 2 and 7 is 2.
Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).
"""


for i in range(int(input())):
    n = int(input())
    numbers = [int(x) for x in input().split()]

    all = 0
    count = 0
    for degree in range(32):
        for num in numbers:
            if num & (1 << degree) == 0:
                count += 1
        all += (len(numbers) - count) * count * 2
        count = 0

    print(int(all % (1e9 + 7)))
