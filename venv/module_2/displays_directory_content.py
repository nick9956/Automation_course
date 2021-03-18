import os
from prettytable import PrettyTable


def directory_content(path):
    dirs = os.listdir(path)
    table = PrettyTable()
    table.field_names = ["Mode", "Owner", "Group", "Size", "File Name"]
    for file in dirs:
        file_stat = os.stat(path)
        table.add_row([file_stat.st_mode, "Mykola Rudym",
                       "tp", file_stat.st_size, file])
    print(table)



directory_content('C:/Users/Mykola_Rudym/Documents/pythonProject/venv/module_2')

