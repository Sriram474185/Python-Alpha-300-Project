nums = [1, 1, 0, 1, 1, 1]
current = 0    
largest = 0    
for i in range(len(nums)):
    if nums[i] == 1:
        current = current + 1
    else:
        current = 0
    if current > largest:
        largest = current

print(largest)