def findInMountainArray(target, mountain_arr):
    def find_peak_index(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(arr, target, left, right, ascending=True):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if ascending:
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if arr[mid] > target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    peak_index = find_peak_index(mountain_arr)
    index = binary_search(mountain_arr, target, 0, peak_index)
    if index != -1:
        return index
    return binary_search(mountain_arr, target, peak_index + 1, len(mountain_arr) - 1, ascending=False)

if __name__ == "__main__":
    
    mountain_arr1 = [1, 2, 3, 4, 5, 3, 1]
    target1 = 3
    print(findInMountainArray(target1, mountain_arr1))  

    mountain_arr2 = [0, 1, 2, 4, 2, 1]
    target2 = 3
    print(findInMountainArray(target2, mountain_arr2))  

    mountain_arr3 = [0, 5, 3, 1]
    target3 = 1
    print(findInMountainArray(target3, mountain_arr3))  