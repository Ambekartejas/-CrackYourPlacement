class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # from collections import Counter
        # x=Counter(nums)
        # for i in nums:
        #     if x[i]>1:
        #         return i
        seen=set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        