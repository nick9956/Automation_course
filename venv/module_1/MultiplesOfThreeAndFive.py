def multiples_of_three_and_five ():

    #numbers = range(1, 100000000)
    #sum_of_multiples = 0

    #for index in numbers:
        #if((index % 3 == 0) and (index % 5 == 0)):
            #sum_of_multiples += index

    #print(sum_of_multiples)

    total = 0
    end = 100000000

    for index_for_three in range(3, end, 3):
        total += index_for_three

    for index_for_five in range(5, end, 5):
        if index_for_five % 3 != 0:
            total += index_for_five

    print(total)