from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in index:
            return [index[c], i]
        index[num] = i
    return []