class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        brr.sort()
        i,j=0,0
        c=0
        while(i<n):
            while(j<n):
                if(arr[i]<=brr[i]):
                    c+=1
                j+=1
                i+=1
        if(c==n):
            return True
        else:
            return False
