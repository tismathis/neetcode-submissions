class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            x = (a >> i) & 1
            y = (b >> i) & 1
            s = x ^ y ^ carry                       # sum bit
            carry = (x & y) | (carry & (x ^ y))     # carry out
            if s:
                res |= (1 << i)                     # set bit i, not bit 0
        if res >= 1 << 31:                          # interpret as signed 32-bit
            res -= 1 << 32
        return res