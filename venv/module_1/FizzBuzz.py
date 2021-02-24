def fizz_buzz ():
    numbers = range(1, 101)
    for display_numbers in numbers:
        if((display_numbers % 3 == 0) and (display_numbers % 5 == 0)):
            display_numbers = 'FizzBuzz'
        elif (display_numbers % 3 == 0):
            display_numbers = 'Fizz'
        elif (display_numbers % 5 == 0):
            display_numbers = 'Buzz'
        print(display_numbers)



