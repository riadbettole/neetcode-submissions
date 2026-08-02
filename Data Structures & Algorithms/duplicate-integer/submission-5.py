class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set()

        for num in nums:
            if num in setNum:
                return True
            setNum.add(num)
            
        return False