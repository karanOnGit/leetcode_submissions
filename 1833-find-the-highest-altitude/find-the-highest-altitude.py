class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = []
        prev = 0
        alt.append(prev)
        for i in gain:
            prev += i
            # print(prev, " ")
            alt.append(prev)

        return max(alt)