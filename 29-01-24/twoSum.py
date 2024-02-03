class Solution:

def twoSum(self, nums: List[int], target: int) -> List[int]:

numsLength = len(nums)

for sum1 in range(nums Length):

for sum2 in range(nums Length):

if sum1 == sum2:

continue

currSum = nums[sum1] + nums[sum2]

if currSum == target: return [sum1, sum2]
