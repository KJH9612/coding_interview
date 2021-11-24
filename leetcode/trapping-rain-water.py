from typing import List


def solve(h: List[int]) -> int:
    if not h:
        return 0

    volume = 0
    left, right = 0, len(h) - 1
    left_max, right_max = h[left], h[right]

    while left < right:
        left_max, right_max = max(h[left], left_max), max(h[right], right_max)

        if left_max <= right_max:
            volume += left_max - h[left]
            left += 1
        else:
            volume += right_max - h[right]
            right -= 1
    return volume


print(solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
