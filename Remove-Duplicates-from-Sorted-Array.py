1class Solution {
2    public int removeDuplicates(int[] nums) {
3        if (nums.length == 0) return 0; // Edge case
4        
5        int j = 0; // Pointer for the position of the last unique element
6
7        for (int i = 1; i < nums.length; i++) {
8            if (nums[i] != nums[j]) { 
9                j++; 
10                nums[j] = nums[i]; // Move unique element forward
11            }
12        }
13        
14        return j + 1; // Length of the unique subarray
15    }
16}
17