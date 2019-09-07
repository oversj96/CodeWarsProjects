def delete_nth(order,max_e):
    order_dict = {}
    for i in order:
        if(i not in order_dict):
            order_dict[i] = 0
    new_order = []
    for x in order:
        if(order_dict[x] < max_e):
            order_dict[x] += 1
            new_order.append(x)
    return new_order


print(delete_nth([5, 27, 4, 40, 2, 45, 5, 5, 45, 5, 5, 40, 45, 5, 2, 5, 5, 40, 40, 45, 40, 2, 5, 5, 5, 2, 5, 45, 5, 27, 5, 45, 5, 5, 4, 27, 5, 5, 5, 5, 4, 40, 4, 5, 5, 45, 5, 40, 45, 5, 4, 45, 40, 40],10))