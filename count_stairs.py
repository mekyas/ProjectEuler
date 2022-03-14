def arrangeCoins(n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            cost = (1 + mid) * mid // 2
            if cost <= n:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
print(arrangeCoins(5))