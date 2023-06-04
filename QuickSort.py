def quickSort(nums, start, end) :
    if start < end :
        partitionIndex = partition(nums, start, end)
        quickSort(nums, start, partitionIndex - 1)
        quickSort(nums, partitionIndex + 1, end)
def partition(nums, start, end) :
    pivot = nums[end]
    partitionIndex = start
    for i in range(start, end, 1) :
        if nums[i] <= pivot :
            nums[i], nums[partitionIndex] = nums[partitionIndex], nums[i]
            partitionIndex += 1
    nums[partitionIndex], nums[end] = nums[end], nums[partitionIndex]
    return partitionIndex

nums = [2, 567, 32, 45645, 232, 4325]

quickSort(nums, 0, len(nums) - 1)
print(nums)
