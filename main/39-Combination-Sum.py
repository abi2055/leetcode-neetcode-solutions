class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(i, total):
            if total == target:
                result.append(combination.copy())
                return 
            if total > target or i >= len(candidates):
                return 

            combination.append(candidates[i])
            dfs(i, total + candidates[i])

            combination.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return result



        