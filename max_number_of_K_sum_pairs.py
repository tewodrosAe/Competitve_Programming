class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0
        for num in nums:
            if count[num] > 0:
                x  = k - num
                count[num] -= 1
                if count[x] > 0:
                    res += 1
                    count[x] -= 1

        return res 
