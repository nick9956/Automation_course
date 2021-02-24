import enum

class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4


def file_size_conversion(size_in_bytes, data_unit):
       if data_unit == SIZE_UNIT.KB:
           return size_in_bytes/1024
       elif data_unit == SIZE_UNIT.MB:
           return size_in_bytes/(1024 * 1024)
       elif data_unit == SIZE_UNIT.GB:
           return size_in_bytes /(1024 * 1024 * 1024)
       else:
           return size_in_bytes


try:
    userInput = int(input("Please enter an integer number of bytes: "))
    select_data_unit = int(
        input("Please enter a number from 1 to 4, depending on which data unit you want to convert file?\n"
              " 1 - BYTES, 2 - KB, 3 - MB, 4 - GB\n"))
    if select_data_unit not in (1, 2, 3, 4):
        raise Exception("You enter number for which data unit is not exist")
except ValueError:
    print("Not an integer! Try again.")

converted_file_size = file_size_conversion(userInput, SIZE_UNIT(select_data_unit))
print("File size is : {0:.2f}".format(converted_file_size) + SIZE_UNIT(select_data_unit).name)