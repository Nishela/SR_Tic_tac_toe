def some(iter_obj):
    for itm in iter_obj:
        for item in itm:
            yield item


def horizont_combinations(iter_object: iter, board_size: int) -> tuple:
    '''
    Функция собирает в кортеж значения в строке
    :param iter_object: итрерируемый объект
    :param board_size: размер игрового поля
    :return:
    '''
    i = 0
    horizont = []
    for itm in range(board_size, board_size * board_size + 1, board_size):
        horizont.append(tuple(iter_object[i:itm]))
        i = itm
    return tuple(horizont)
