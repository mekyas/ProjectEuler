def decodeString(s: str) -> str:
    if not s:
        return ''
    if s[0].isalpha():
        return s[0] + decodeString(s[1:])
    if s[0].isdigit():
        i = 1
        while s[i]!='[':
            i+=1
        start = i
        opened = 1
        i +=1
        while opened>0:
            if s[i]=='[':
                opened+=1
            elif s[i] ==']':
                opened-=1
            i+=1
        end = i
        return int(s[:start])*decodeString(s[start+1:end-1]) + decodeString(s[end:])

print(decodeString('3[a2[c]]'))