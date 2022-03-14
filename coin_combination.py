def solution(coin_list, price):
    # initialize
    correct_list = []
    sorted_list = sorted(coin_list, reverse=True)
    # calculate
    func([], sorted_list, 0, price, correct_list)
    # output
    print('All coin combinations below:')
    result = -1
    for c in correct_list:
        if result < 0 or len(c) < result:
            result = len(c)
        print(' {}'.format(c))
    # result
    return result

def func(current_list, coin_table, start_index, price, correct_list):
    current_sum = sum(current_list)
    for i in range(start_index, len(coin_table)):
        if current_sum + coin_table[i] < price:
            func([*current_list, coin_table[i]], coin_table, i, price, correct_list)
        elif current_sum + coin_table[i] == price:
            correct_list.append([*current_list, coin_table[i]])
            return

if __name__ == "__main__":
    price = 11
    coins = [7, 3, 13]
    print('price: {}'.format(price))
    print('coins: {}'.format(coins))

    result = solution(coins, price)
    print('result: {}'.format(result))