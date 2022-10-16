def str_in_list(sample_list: list) -> str:
    my_string = ''
    for element in sample_list:
        if isinstance(element, str) == 1:
            my_string = my_string + element[-1]
    return my_string
