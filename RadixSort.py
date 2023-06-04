def countingSort(nums, place) :
    count = [0] * 10
    output = [0] * len(nums)
    for i in range(len(nums)) :
        index = (nums[i] // place) % 10
        count[index] += 1
    for i in range(1, 10) :
        count[i] += count[i - 1]
    n = len(nums) - 1
    while n >= 0 :
        index = (nums[n] // place) % 10
        output[count[index] - 1] = nums[n]
        count[index] -= 1
        n -= 1
    for i in range(len(nums)) :
        nums[i] = output[i]

def radixSort(nums) :
    maxElem = max(nums)
    place = 1
    while maxElem // place > 0 :
        countingSort(nums, place)
        place *= 10
    


nums = [121, 432, 564, 23, 1, 45, 788]

radixSort(nums)
print(nums)
