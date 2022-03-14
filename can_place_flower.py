from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        possible = 0
        flowerbed = [0]+flowerbed+[0]
        c = 0
        i = 0
        n = len(flowerbed)
        while i<n:
            if flowerbed[i]==0:
                c+=1
            elif flowerbed[i]==1:
                c=0
            if c==3:
                possible+=1
            if possible==n:
                return True
            i+=1
        return possible==n

print(canPlaceFlowers([1, 0, 0, 0, 1], 1))