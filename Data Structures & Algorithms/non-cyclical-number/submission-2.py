class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquaresDigits(m: int) -> int:
            total = 0
            while m:
                m, digit = divmod(m, 10)
                total += (digit ** 2)
            return total

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sumSquaresDigits(n)
        
        return n == 1
        