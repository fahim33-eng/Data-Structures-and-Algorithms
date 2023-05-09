def swap(nums, i, j) :
    nums[i], nums[j] = nums[j], nums[i]

def siftDown(nums, i, upper) :
    while True :
        l, r = (i * 2) + 1, (i * 2) + 2
        if max(l, r) < upper :
            if nums[i] > max(nums[l], nums[r]) :
                break
            elif nums[l] > nums[r] :
                swap(nums, i, l)
                i = l
            else :
                swap(nums, i, r)
                i = r 
        elif l < upper :
            if nums[l] > nums[i] :
                swap(nums, i, l)
                i = l
            else :
                break
        elif r < upper :
            if nums[r] > nums[i] :
                swap(nums, i, r)
                i = r
            else :
                break
        else :
            break
def heapSort(nums) :
    for j in range((len(nums) - 2) // 2, -1, -1) :
        siftDown(nums, j, len(nums))
    
    for end in range(len(nums) - 1, 0, -1) :
        swap(nums, 0, end)
        siftDown(nums, 0, end)
    return nums


nums = heapSort([5, 2, 123, 44, 1, 4])

print(nums)