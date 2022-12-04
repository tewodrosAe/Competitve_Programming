class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0
        for num in count: 
            if count[num] > 1:
                count[num] -= 1
                while count[num] > 0:
                    total += count[num]
                    count[num] -= 1
        return total
