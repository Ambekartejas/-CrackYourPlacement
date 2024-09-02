class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=1
        i=0
        while j<len(nums):
            if nums[i]==0:
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        