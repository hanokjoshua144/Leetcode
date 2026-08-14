class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new1=[]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in new1:
                    new1.append(nums1[i])


        return new1