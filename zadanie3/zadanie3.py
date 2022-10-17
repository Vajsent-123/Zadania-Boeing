def b_in_a(list_a: list, list_b: list) -> list:
    element_count = {}
    true_or_false_list = []
    for element in list_b:
        element_count[element] = 1
    for element in list_a:
        if element in element_count:
            true_or_false_list.append(True)
        else:
            true_or_false_list.append(False)
    return true_or_false_list
