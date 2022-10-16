
def b_in_a(list_a: list, list_b: list) -> list:
    my_list = []
    for m in list_a:
        if m in list_b:
            my_list.append(True)
        else:
            my_list.append(False)
    return my_list

