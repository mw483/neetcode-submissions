class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for num in nums:
            if num not in appeared:
                appeared.add(num)
            else:
                return True
        return False
        
            
        