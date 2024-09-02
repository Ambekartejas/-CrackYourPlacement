class Solution:
    from collections import Counter
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zero,ones=0,0
        for i in range(n):
            if nums[i]==0:
                zero+=1
            elif nums[i]==1:
                ones+=1

        for i in range(zero):
            nums[i]=0
        for i in range(zero,zero+ones):
            nums[i]=1
        for i in range(zero+ones,n):
            nums[i]=2
        
        # for i in range(n):
        #     min1=i
        #     for j in range(i+1,n):
        #         if nums[j]<nums[min1]:
        #             min1=j
        #     nums[i],nums[min1]=nums[min1],nums[i]
        return nums