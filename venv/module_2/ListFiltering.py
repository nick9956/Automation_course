def list_filtering_with_for_option():
    initial_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

    for index_two in initial_list[:]:
        if type(index_two) is not int:
            initial_list.remove(index_two)
    print(initial_list)

def list_filtering_with_comprehenstion_list_option():
    initial_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    new_list = [index for index in initial_list if type(index) is int]
    print(new_list)

def list_filtering_third_with_lambda_option():
    initial_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    new_list = list(filter(lambda index: type(index) is int, initial_list))
    print(new_list)

list_filtering_with_for_option()
list_filtering_with_comprehenstion_list_option()
list_filtering_third_with_lambda_option()
