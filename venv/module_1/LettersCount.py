def letters_count():
    text = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!
'''

    Letter_counter = {}

    python_count = text.count("Python")
    for index in text.lower():
        if index.isalpha():
            if index in Letter_counter:
                Letter_counter[index] += 1
            else:
                Letter_counter[index] = 1

    most_common_letter = max(Letter_counter, key=Letter_counter.get)
    count_of_the_most_common_letter = max(Letter_counter.values())


    print ('The most common letter is: ' + most_common_letter)
    print(f'The count of this letter is {count_of_the_most_common_letter}')
    print(f'The word Python occurs {python_count} times in the text')

letters_count()
