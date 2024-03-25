def contains_list(number_list1, number_list2):
    # return list(map(number_list1.__contains__, number_list2))
    # return [number_list1.__contains__(x) for x in number_list2]
    # return [number in number_list1 for number in number_list2]
    return [number for number in number_list1 if number in number_list2]

def add_lists(number_list1, number_list2):
    return list(map(list.__add__, number_list1, number_list2))



# print(add_lists([[1, 3], [5, 7], [9, 11]], [[2, 4], [6, 8], [10, 12, 14]]))
print(contains_list([1, 2, 3], [1, 2, 3, 4, 5]))
