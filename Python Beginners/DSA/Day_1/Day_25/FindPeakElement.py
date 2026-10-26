def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1 
        else:
            right = mid  

    return left  

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 1]
    print(findPeakElement(nums1))  

    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums2))  