
def kaupk_daugyba(*args)
    if not args:
        return 0

    if len(args) == 1:
        return args[0]

    kaupiklis = args[0]
    for elem in args[1:]:
        kaupiklis *= elem
    return kaupiklis


def kaupk_aritmetika(*args, operacija='suma'):

    if not args:
        return 0

    if len(args) == 1:
        return args[0]

    res = args[0]
    for elem in args[1:]:
        if operacija == 'suma':
            res += elem
        if operacija == 'atimtis':
            res -= elem
        if operacija == 'dalyba':
            res /= elem
        if operacija == 'daugyba':
            res *= elem
    return res
