class Solution:
    def replaceElements(self, arr):
        great =arr[-1]
        for i in range(len(arr)-2,-1,-1):
            current = arr[i]
            arr[i]= great
            great= max(great,current)
        arr[-1]=-1
        return arr