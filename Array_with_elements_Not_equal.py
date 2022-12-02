class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        number=[]
        length = len(nums)
        l,r = 0,length-1
        while len(number) < length:
            number.append(nums[l])
            l += 1
            if l < r:
                number.append(nums[r])
                r -= 1
        return number
