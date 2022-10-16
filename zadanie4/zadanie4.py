



def models_in_codes(models: list, codes: dict) -> list:
    my_list = []
    for i in models:
        if i in codes.keys():
            my_list.append(codes[i])
    return my_list





