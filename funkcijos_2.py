
def kaupk_daugyba(*args: int | float) -> int | float:
    if not args:
        return 0

    if len(args) == 1:
        return args[0]

    kaupiklis = args[0]
    for elem in args[1:]:
        kaupiklis *= elem
    return kaupiklis



def sudaugink_visus_is_pirmo(skaicius, *args):
    if not args:
        kaupiklis = [skaicius]
    else:
        kaupiklis = []
    for elem in args:
        kaupiklis.append(skaicius * elem)
    return kaupiklis