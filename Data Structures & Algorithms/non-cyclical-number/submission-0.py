class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquaresDigits(m: int) -> int:
            total = 0
            while (True):
                m, digit = divmod(m, 10)
                total += (digit ** 2)
                if m == 0:
                    return total


        seen = {n}

        while n != 1:
            n = sumSquaresDigits(n)
            if n in seen:
                return False
            seen.add(n)
        
        return True