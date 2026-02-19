1class Solution(object):
2    def intersection(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: List[int]
7        """
8        
9        intersection_list = []
10
11        for i in range(len(nums1)):
12            for c in range(len(nums2)):
13                if nums1[i] == nums2[c]:
14                    intersection_list.append(nums1[i])
15                    break
16
17        remove_dupes = set(intersection_list)
18        return list(remove_dupes)
19
20        
21