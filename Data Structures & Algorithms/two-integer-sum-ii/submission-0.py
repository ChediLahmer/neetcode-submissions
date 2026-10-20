class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _min = 0
        _max = len(numbers) -1
        notFound = True
        while _max!=_min and notFound :
            _sum = numbers[_min] + numbers[_max]
            if _sum == target:
                return [_min+1, _max+1]
            else:
                if _sum < target:
                    _min+=1
                elif _sum > target:
                    _max-=1

        return []