zero = nums.count(0)
one = nums.count(1) + zero
two = nums.count(2)
for i in range(len(nums)):
    if i < zero:
        nums[i] = 0
    else:
        if i < one:
            nums[i] = 1
        else:
            nums[i] = 2
