def maxProfit(prices) -> int:
        from itertools import combinations_with_replacement 
        comb = combinations_with_replacement([1, -1, 0], len(prices))
        good_comb = []
        for elt in comb:
            if sum(elt)==0:
                good_comb.append(elt)
        best =0
        print(good_comb)
        for elt in good_comb:
            profit = sum(i*j for i,j in zip(prices, elt))
            best = max(profit, best)
        return best
print(maxProfit([1, 2, 3, 0, 2]))