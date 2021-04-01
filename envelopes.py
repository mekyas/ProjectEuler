"""Programming Problem:
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope
is greater than the width and height of the other envelope.
write a code that returns the maximum number of envelopes that can be put one inside other.
Example:
Input: [[5, 4], [6, 4], [6, 7], [2, 3]]
Output: 3
Explanation : [2, 3] => [5, 4] => [6. 7]
"""


from typing import List
import bisect

def solution(envelopes: List[List])->int:
    envelopes.sort(key= lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        indx = bisect.bisect_left(dp, h)
        if indx==len(dp):
            dp.append(h)
        else:
            dp[indx]=h
    return len(dp)



if __name__=="__main__":
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(solution(envelopes))
