def unpack(input_tuple):
    list_test = []
    for i in input_tuple:
        if isinstance(i, tuple):
            for j in i:
                list_test.append(j)
        else:
            list_test.append(i)
    return tuple(list_test)

# example:  hobbies_Adam = ('reading', ('jogging', ('boxing'), 'yoga'), 'movies')
#           print(unpack(hobbies_Adam))
