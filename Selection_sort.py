
class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min = i
            for j in range(i,n):
                if arr[min] > arr[j]:
                    min = j
            arr[min],arr[i] = arr[i],arr[min]
