def partitionLabels(S: str):
        
        intervals = {}
        for i, letter in enumerate(S):
            if letter in intervals:
                intervals[letter]=[intervals[letter][0], i]
            else:
                intervals[letter]=[i, i]
        start_end = sorted(intervals.values())
        n = len(start_end)
        result = []
        i = 0
        while i<n:
            start, end = start_end[i]
            j = i+1
            while j<n and start_end[j][0]<end:
                if start_end[j][1]>end:
                        end = start_end[j][1]
                j+=1
            result.append(end-start+1)
            i = j
        return result

print(partitionLabels("ababcbacadefegdehijhklij"))