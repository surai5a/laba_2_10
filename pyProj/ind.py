#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum(*nums):
    if not nums:
        return None
    else:
        numbers = [int(num) for num in nums]
        max = -1
        ind = int
        sum = 0
        for i, num in enumerate(numbers):
            if num > max:
                ind = i
        for i, num in enumerate(numbers):
            if (i != ind) and (num > 0):
                sum += num
        return sum


if __name__ == "__main__":
    print(sum(1, 2, -3, 7, 10))
