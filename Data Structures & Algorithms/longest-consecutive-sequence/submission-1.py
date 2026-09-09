class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
          return 0

        data = set(nums)
        
        sequences_start = set()
        for element in data:
          if element-1 not in data:
            sequences_start.add(element)

        max_length = 1
        for element in sequences_start:
          sequence_dead = False
          current_length = 1
          while not sequence_dead:
            if element+current_length not in data:
              sequence_dead=True
              if current_length > max_length:
                max_length = current_length
            else:
              current_length+=1
        return max_length