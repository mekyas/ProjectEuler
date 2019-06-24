from bisect import bisect_left
num_limits = [1, 5, 10, 50, 100, 500, 1000]
spec_num = [4, 9, 40, 90, 400, 900]
roman ='IVXLCDM'
spec_roman =['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
def intToRoman(num): 
    result = ''
    n = len(str(num))
    for i in range(n):
        temp = int(str(num)[i])*10**(n-i-1)
        while temp != 0:

            if temp in num_limits:
                idx = bisect_left(num_limits, temp)
                result += roman[idx]
                temp -= num_limits[idx]
            elif temp in spec_num:
                idx = bisect_left(spec_num, temp)
                result += spec_roman[idx]
                temp -= spec_num[idx]
            else:
                idx = bisect_left(num_limits, temp)-1
                result += roman[idx]
                temp -= num_limits[idx]
    return result


print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))