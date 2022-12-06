class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        for i in range(len(piles)//3):
            length = len(piles) - 1
            piles.pop()
            take =  piles.pop()
            res += take
            
        return res