class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        _res = [1]*(len(nums))
        for index in range(len(nums)):
          _res[index] =prefix
          prefix*=nums[index]

        for index in range(len(nums)-1, -1, -1):
          _res[index]*=suffix
          suffix*=nums[index]
        return _res