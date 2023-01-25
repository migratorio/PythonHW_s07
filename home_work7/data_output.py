def output_data(data):
    if len(data) > 0:
        for item in data:
            print('\n')
            for i in range(0, 5):
                print(item[i].ljust(15), end='')
    else:
        print("Справочник пуст!")
