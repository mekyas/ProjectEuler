def intervalIntersection(A, B):
        def combine_interval(interval1, interval2):
            "combine two intervals"
            a, b = interval1
            c, d = interval2
            if b<c :
                return False
            elif b==c:
                return [b, b]
            else:
                return [c, min(b, d)]
        
        combined = []
        l1 = len(A)
        l2 = len(B)
        i1 = i2 = 0
        if l2==0 or l1==0:
            return []
        while i1<l1 and i2< l2:
            if A[i1][0]<B[i2][0]:
                combined.append(A[i1])
                i1+=1
            else:
                combined.append(B[i2])
                i2+=1
        while i1<l1:
            combined.append(A[i1])
            i1+1
        while i2<l2:
            combined.append(B[i2])
            i2+=1
        ans = []
        for i in range(len(combined)-1):
            c = combine_interval(combined[i], combined[i+1])
            if c:
                ans.append(c)
        return ans

print(intervalIntersection([[3, 10]], [[5, 10]]))