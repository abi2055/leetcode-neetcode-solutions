class Solution:
    def isPalindrome(self, s: str) -> bool:

        # string.replace(" ", ""), first param is what its looking for
        # second param is the replacement 

        clean = "".join(ch for ch in s if ch.isalnum())
        no_spaces = clean.lower()

        print(no_spaces)

        first_pointer = 0
        last_pointer = len(no_spaces)

        for i in range(len(no_spaces)):
            print("First Pointer: ", first_pointer)
            print("Last Pointer: ", last_pointer)
            if no_spaces[first_pointer] != no_spaces[last_pointer - 1]:
                break
            elif first_pointer == (last_pointer + 1):
                return True
            first_pointer += 1
            last_pointer -= 1

        return False

        