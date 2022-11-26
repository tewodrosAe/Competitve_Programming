class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = []
        def sort(arr,first,last):
            if first >= last:
                return(arr)
            else:
                i = first
                j = last - 1
                while i < j:
                    if arr[i] >= arr[last] and arr[j] <= arr[last]:
                        arr[i],arr[j] = arr[j],arr[i]
                        j -= 1
                        i += 1
                    if arr[i] < arr[last]:
                        i += 1
                    if arr[j] > arr[last]:
                        j -= 1
                if arr[i] > arr[last]:
                    arr[i],arr[last] = arr[last],arr[i]
                    sort(arr,first,i-1)
                    sort(arr,i+1,last) 
                else:
                    arr[i+1],arr[last] = arr[last],arr[i+1]
                    sort(arr,first,i)
                    sort(arr,i+2,last) 
                return arr
        arr = sort(nums,0,len(nums)-1)
        for i in range(len(arr)):
            if arr[i] == target:
                count.append(i)
        return count
