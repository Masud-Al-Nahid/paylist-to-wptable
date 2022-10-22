import csv
import json
from subprocess import list2cmdline
html_output = []
names = []


def pylist_to_list(list):
    temp_list = ['<ul>']
    for element in list:
        temp_list.append(f'<li>{element}</li>')

    temp_list.append('</ul>')
    html_string = ''.join(temp_list)
    return html_string


# This 'my_list.csv' file have bunch line of data list
with open('my_list.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    # Ingredients is header name
    for line in csv_data:
        if line['Ingredients'] == 'No Reward':
            break
        names.append(f"{line['Ingredients']}")


for name in names:
    name = name.replace(']', '').replace('[', '').replace('\'', '"')
    ingredient_list = name.split('"')

    while '' in ingredient_list:
        ingredient_list.remove('')

    while ', ' in ingredient_list:
        ingredient_list.remove(', ')

    single_element = pylist_to_list(ingredient_list)
    html_output.append(single_element)

    with open('final.csv', 'w') as f:
        for line in f:
            writer = csv.writer(line)
            writer.writerow(html_output[0])     
print(html_output[0])

