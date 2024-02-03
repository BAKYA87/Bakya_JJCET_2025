class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                res = [1]
                for num in nums:
                    
                    res.append(res[-1]*num)
                    b = 1   
                for i in range(len(nums)):
                    res[len(nums)-i-1] = res[len(nums)-i-1] * b
                    b = b* nums[len(nums)-i-1]
            
                return res[0:-1]
