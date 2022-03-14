def solution(envel_list):
    # initialize
    sorted_list = sorted(envel_list, key=lambda e: e.width, reverse=True)
    print([[e.width,e.height] for e in sorted_list])
    # process
    arranged_list = []
    for e in sorted_list:
        for a in arranged_list:
            if e.height < a.height and e.width < a.width and a.layer + 1 > e.layer:
                e.parent = a
                e.layer = a.layer + 1
        arranged_list.append(e)

    return arranged_list

class Envelopes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.parent = None
        self.layer = 1

if __name__ == "__main__":
    data = [[5,4], [23,1], [7,8], [3,52], [9,10], [10,9], [6,4], [6,7], [2,3]]
    envel = [Envelopes(d[0], d[1]) for d in data]

    result_list = solution(envel)

    # print input
    print('input: ')
    print("{}\n".format(data))

    # print result
    e = sorted(result_list, key=lambda e: e.layer, reverse=True)[0]
    print('output: {0}'.format(e.layer))
    while True:
        print('[{0},{1}]'.format(e.width, e.height))
        e = e.parent
        if e is None:
            break