class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # starting at the front you expand pointer 2 
        # until k is satisfied
        # until k is unsatisfied you expan again
        # when k is unsatsified you shrink from left
        # and compare against max 

        # concepts a dictionary to keep a frequency count
        # a stack to push digits onto 
        n = len(s)
        left = 0
        count = 0
        best = ""

        for right in range(n):
            if s[right] == "1":
                count += 1

            # once we have exactly k ones, shrink from the left
            # as far as possible while keeping count == k
            while count == k:
                candidate = s[left:right + 1]
                if best == "" or len(candidate) < len(best) or (len(candidate) == len(best) and candidate < best):
                    best = candidate

                if s[left] == "1":
                    count -= 1
                left += 1

        return best