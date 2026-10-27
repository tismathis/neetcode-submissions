class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = []

        for i in range(n + 1):
            counterOf1 = 0
            for j in range(32):
                if (1 << j) & i:
                    counterOf1 += 1
            counter.append(counterOf1)

        return counter