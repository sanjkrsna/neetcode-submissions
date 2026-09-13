class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((pile + k - 1) // k for pile in piles)  # ceil(pile / k) using integer arithmetic

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if hours_needed(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low

        