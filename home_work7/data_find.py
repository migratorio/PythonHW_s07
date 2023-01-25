from re import search


def find_data(f_d, data):
    if len(data) > 0:
        for item in data:
            for el in item:
                if search(f_d, el):
                    return item
    else:
        return None
