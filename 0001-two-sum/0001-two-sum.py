class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        mapi={}
        for i in range(n):
            if target-nums[i] in mapi:
                return [i,mapi[target-nums[i]]]
            mapi[nums[i]]=i
        return -1
        
        
        