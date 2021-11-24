from typing import List

def solve(nums: List[int]) -> List[int]:
    tmp = 1
    lst = []

    for i in range(0, len(nums)):
        lst.append(tmp)
        tmp = tmp * nums[i]

    tmp = 1
    for i in range(len(nums) - 1, -1, -1):
        lst[i] = lst[i] * tmp
        tmp = tmp * nums[i]

    return lst

print(solve([4, 3, 2, 1]))