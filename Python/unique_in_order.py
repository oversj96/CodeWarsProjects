def unique_in_order(iterable):
    order = []
    char = None
    for i in iterable:
        if (char != i):
            char = i
            order.append(i)
    return order
