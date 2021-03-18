INITIAL_LIST = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

def list_filtering_with_for_option():

    for index_two in INITIAL_LIST[:]:
        if type(index_two) is not int:
            INITIAL_LIST.remove(index_two)
    print(INITIAL_LIST)

def list_filtering_with_comprehenstion_list_option():

    new_list = [index for index in INITIAL_LIST if type(index) is int]
    print(new_list)

def list_filtering_third_with_lambda_option():

    new_list = list(filter(lambda index: type(index) is int, INITIAL_LIST))
    print(new_list)

list_filtering_with_for_option()
list_filtering_with_comprehenstion_list_option()
list_filtering_third_with_lambda_option()
