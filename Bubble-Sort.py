count = 0
length = len(a) 
sorted = False
while not sorted:
    sorted = True
    for j in range(length - 1):
        if a[j] > a[j+1]:
            count = count + 1
            a[j],a[j+1] = a[j+1],a[j]
            sorted = False

print("Array is sorted in" , count , "swaps.")
print("First Element:" ,a[0])
print("Last Element:" , a[length-1])
