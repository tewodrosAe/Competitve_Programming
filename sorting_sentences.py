class Solution:
    def sortSentence(self, s: str) -> str:
        ars = list(s.split(" "))
        arr = [None for i in range(len(ars))]
        add = ""
        for letters in s:
            if letters.isnumeric():
                arr[int(letters)-1] = add
                add = ""
            elif letters == ' ':
                pass
            else:
                add += letters
        
        return (" ").join(arr)
