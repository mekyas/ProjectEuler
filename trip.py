import sys

def min_exchange(expenses):
    right_exp = sum(expenses)/len(expenses)
    right_exp = round(right_exp, 2)
    diff = [x- right_exp for x in expenses]
    neg_sum = 0
    pos_sum = 0
    for i in range(len(diff)):
        if diff[i]> 0:
            pos_sum += diff[i]
        else:
            neg_sum += diff[i]
    return -neg_sum if -neg_sum < pos_sum else -neg_sum
