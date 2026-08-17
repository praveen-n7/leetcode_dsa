class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k= m-1,n-1,m+n-1 # set the pointers at the end of each lists and also the end of the final list of nums1
        while j>=0: #as long as there are elements to be addressed in th nums2 list
            if i>=0 and nums1[i]>nums2[j]:#compare i and j elements of nums1 and nums2 
                nums1[k]=nums1[i]; i-=1
            else:
                nums1[k]=nums2[j]; j-=1
            k-=1 #anyways the above condition hits k must be reduced for next 2nd largest element to be inserted 
        