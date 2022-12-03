class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i,n in enumerate(nums):
            nums[i] = int(n)
        nums.sort(reverse=True)
        return str(nums[k-1])
