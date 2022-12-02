class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        def compares(n,n1):
            if n+n1 > n1+n:
                return -1
            else:
                return 1
        nums = sorted(nums,key = cmp_to_key(compares))
        return str(int("".join(nums)))


      
      
