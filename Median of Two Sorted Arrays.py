"""
This a solution for the problem from
https://leetcode.com/problems/median-of-two-sorted-arrays/

Here is the copy of the problem from leetcode:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def applyRecursiveRule(i,j,nums1,nums2,k):
            r=nums1[i-1]
            s=nums2[j-1]
            if r<s :
                if i==len(nums1):
                    return findkthSortedArrays([], nums2,k-i)
                return findkthSortedArrays(nums1[i:], nums2,k-i)
            else:
                if i==len(nums2):
                    return findkthSortedArrays(nums1,[],k-j)
                return findkthSortedArrays(nums1, nums2[j:],k-j)
            
        def findkthSortedArrays(nums1: List[int], nums2: List[int],k):
            
            #Apply edge cases
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            
            if k==0:
                return min(nums1[0],nums2[0])
            if k==1:
                if len(nums1)==1:
                    h=nums2[0]
                else:
                    h=min(nums1[1],nums2[0])
                if len(nums2)==1:
                    r=nums1[0]
                else:
                    r=min(nums1[0],nums2[1])
                return max(r,h)
            
            if len(nums1)<int(k/2):
                return applyRecursiveRule(len(nums1),k-len(nums1),nums1,nums2,k)
            if len(nums2)<int(k/2):
                return applyRecursiveRule(k-len(nums2),len(nums2),nums1,nums2,k)
            
            return applyRecursiveRule(int(k/2),int(k/2),nums1,nums2,k)
        
        k=len(nums1)+len(nums2)
        if k%2==1:
            return findkthSortedArrays(nums1, nums2,int(k/2))
        else:
            g=findkthSortedArrays(nums1, nums2,int(k/2)-1)
            h=findkthSortedArrays(nums1, nums2,int(k/2))
            return (g+h)/2
