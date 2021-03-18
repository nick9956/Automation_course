import csv
import json

with open('./other_files/cars.csv', newline='') as csvfile:
    json_list = []
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        json_list.append(row)

with open(r'./other_files/cars.json', 'w', encoding='utf-8') as jsonf:
    json_string = json.dumps(json_list, indent=2)
    jsonf.write(json_string)