def find_min_and_max():
    numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    for index in range(len(numbers)):
        if type(numbers) is not int:
            try:
                numbers[index] = int(numbers[index])
            except ValueError:
                pass
            except TypeError:
                pass

    just_numbers =  [index for index in numbers if type(index) is int]


    print(just_numbers)
    print(f"Max value: {max(just_numbers)} and min value: {min(just_numbers)}")

find_min_and_max()