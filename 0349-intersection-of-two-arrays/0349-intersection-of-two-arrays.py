class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = sorted(set(nums2))
        def has(x):
            l,r =0,len(nums2)-1
            while l<=r:
                m=(l+r)//2
                if nums2[m]==x: return True
                if nums2[m]<x:l=m+1
                else:r=m-1
            return False
        return [x for x in set(nums1) if has(x)] #checks in nums1 list for all vlaues of nums2 set using the defined has(x) function,it passes all the values of nums1 in has(x)

        