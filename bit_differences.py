t = int(input())

for i in range(t):
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
