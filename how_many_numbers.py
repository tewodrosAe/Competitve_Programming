class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = [0 for i in range(length)]
        count = 0
        for i in range(length):
            count = 0
            for j in range(length):
                if nums[j] < nums[i]:
                    count += 1
            arr[i] = count
        
        return arr
