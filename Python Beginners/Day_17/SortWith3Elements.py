def sort3elements(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [2, 0, 2, 1, 1, 0]
    print(sort3elements(nums1))  

    nums2 = [2, 0, 1]
    print(sort3elements(nums2))