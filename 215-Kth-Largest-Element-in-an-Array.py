class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)