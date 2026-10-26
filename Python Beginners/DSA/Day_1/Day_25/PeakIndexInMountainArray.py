def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  
        else:
            right = mid  

    return left  

if __name__ == "__main__":
    
    arr1 = [0, 1, 0]
    print(peakIndexInMountainArray(arr1))  

    arr2 = [0, 2, 1, 0]
    print(peakIndexInMountainArray(arr2)) 

    arr3 = [0, 10, 5, 2]
    print(peakIndexInMountainArray(arr3))