def find_min_and_max():
    numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    for index in range(len(numbers)):
        if type(numbers) is not int:
            try:
                numbers[index] = int(numbers[index])
            except ValueError:
                print('It is not digit')
            except TypeError:
                pass

    sorted_numbers = sorted(list(filter(lambda x: type(x) == int, numbers)))

    print(numbers)
    print(f"Max value: {sorted_numbers[-1]} and min value: {sorted_numbers[0]}")
