class Solution:
    def reverseArray(self, arr):
        # code here
        a=0
        n=len (arr)
        for i in range(n//2):
            a=arr[i]
            arr[i]=arr[n-1-i]
            arr[n-1-i]=a