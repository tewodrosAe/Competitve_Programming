class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) <= 1 or len(changed) % 2 != 0:
            return []
        else:
            count = Counter(changed)
            changed.sort()
            original = []
            i = 0
            j = len(changed)-1
            l = 0
            for num in changed:
                if num == 0 and count[num] >= 2:
                    original.append(num)
                    count[num] -= 2
                elif num > 0 and count[num] and count[num*2]:
                    original.append(num)
                    count[num] -= 1
                    count[num*2] -= 1
            return original if len(original) == len(changed)//2 else []
