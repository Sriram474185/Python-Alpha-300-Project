class Solution:
    def getSecondLargest(self, arr):
        # code here
        n=len(arr)
        l_element=arr[0]
        s_element=-1
        for i in range(0,n):
            if (arr[i]>l_element):
                s_element=l_element
                l_element=arr[i]
            elif (arr[i]<l_element and arr[i]> s_element):
                s_element=arr[i]
        return s_element