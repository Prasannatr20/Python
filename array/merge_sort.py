class Solution:
    def merge_sort(self, arr):
        if len(arr)>1:
            middle = len(arr)//2
            left = arr[:middle]
            right = arr[middle:]

            self.merge_sort(left)
            self.merge_sort(right)

            lp=rp=fp=0

            while(lp<len(left) and rp<len(right)):
                if left[lp]< right[rp]:
                    arr[fp]= left[lp]
                    lp+=1
                else:
                    arr[fp]= right[rp]
                    rp+=1
                fp+=1

            while(lp<len(left)):
                arr[fp] = left[lp]
                lp+=1
                fp+=1
            while(rp<len(right)):
                arr[fp] = right[rp]
                rp +=1
                fp +=1





arr=[4,2,1,3]
sol= Solution()
sol.merge_sort(arr)
print(arr)