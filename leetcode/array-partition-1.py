from typing import List


def solve(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


print(solve([1, 4, 3, 2]))