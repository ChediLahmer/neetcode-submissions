class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen.get(target - nums[i]),i]
            else:
                seen.update({nums[i] : i})
        return []