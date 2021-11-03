def some(iter_obj):
    for itm in iter_obj:
        for item in itm:
            yield item


def horizont_combinations(iter_object, board_size):
    i = 0
    horizont = []
    for itm in range(board_size, board_size * board_size + 1, board_size):
        horizont.append(tuple(iter_object[i:itm]))
        i = itm
    return tuple(horizont)
