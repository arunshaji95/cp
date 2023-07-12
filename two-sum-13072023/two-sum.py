class Solution:
    def twoSum(self, nums, target):
        hashMap = dict()
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashMap:
                return [i, hashMap[complement]]
            else:
                hashMap[v] = i
            
s = Solution()
print(s.twoSum([3, -1, 0], 3))