class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {item: index for index, item in enumerate(nums)}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in hashmap and hashmap[difference] != i:
                return [i, hashmap[difference]]
