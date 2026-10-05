class Solution:
    def checkValidString(self, s: str) -> bool:
        left_is = []
        star_is = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left_is.append(i)
            elif c == '*':
                star_is.append(i)
            else: # `)`
                if bool(left_is):
                    left_is.pop()
                elif bool(star_is):
                    star_is.pop()
                else:
                    return False
            
        # we have a problem if the `*` occurs before the `(`
        while left_is and star_is:
            if left_is.pop() > star_is.pop():
                return False

        return not bool(left_is)

        