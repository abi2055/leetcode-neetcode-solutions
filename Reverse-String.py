1class Solution {
2    public void reverseString(char[] s) {
3        int count = 0;
4        char storedLetter;
5        for (int i = 0; i < s.length/2; i++) {
6            storedLetter = s[i];
7            s[i] = s[s.length - 1 - count];
8            s[s.length - 1 - count] = storedLetter;
9            count++;
10        }
11    }
12}