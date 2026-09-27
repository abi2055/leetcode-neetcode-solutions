class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                results.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            # this is required for the base case [] being appended

            dfs(i + 1, subset)

        dfs(0, [])
        return results 
        
        