class Solution(object):
    def twoSum(self, nums, target):
        k=int()
        p=[]
        for i in range(len(nums)):
            k=target-nums[i]
            for j in range(i+1,len(nums)):
                if k==nums[j]:
                    p.append(i)
                    p.append(j)
        return p    
