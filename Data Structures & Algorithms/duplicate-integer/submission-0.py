class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = []
        for i in range(len(nums)):
            if nums[i] not in appeared:
                appeared.append(nums[i])
            else:
                return True
        return False
        
            
        