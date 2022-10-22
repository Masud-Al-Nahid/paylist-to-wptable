import requests
from subprocess import list2cmdline
import csv
import json

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
    
#for row in html_output:
    with open('final.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        header = ['Ingredients']
        writer.writerow(header)
        for x in range(0,7):
            writer.writerow(html_output)
              
