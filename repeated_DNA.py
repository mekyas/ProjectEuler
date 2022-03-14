from typing import List

def findRepeatedDnaSequences(s: str) -> List[str]:
        if len(s)<11:
            return []
        letters_val = {'A': '1', 'C':'2', 'G': '3', 'T':'4'}
        s_num = [letters_val[i] for i in s]
        values = {}
        result = set()
        v = s_num[:10]
        values[int(''.join(v))] = 0
        for i in range(1, len(s)-9):
            v.pop(0)
            v.append(s_num[i+9])
            val = int(''.join(v))
            if val in values:
                result.add(values[val])
            else:
                values[val] = i
        ans = []
        for i in result:
            ans.append(s[i:i+10])
        return ans


print(findRepeatedDnaSequences("AAAAAAAAAAA"))