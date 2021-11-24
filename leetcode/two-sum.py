from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    # Brute-Force O(n^2)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # in O(n^2) 내부 함수 좀 더 빠름
   # for i, n in enumerate(nums):
   #      comp = target - n
   #      if comp in nums[i + 1:]:
   #          return [nums.index(n), nums[i + 1:].index(comp) + (i + 1)]

    nums_dict = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict and i != nums_dict[target-num]:
            return [i, nums_dict[target - num]]
        nums_dict[num] = i


print(solve([2, 7, 11, 15], 9))
