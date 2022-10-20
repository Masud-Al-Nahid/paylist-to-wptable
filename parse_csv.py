import csv

html_output = ''
names = []

#This 'my_list.csv' file have bunch line of data list 
with open('my_list.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    #Ingredients is header name
    for line in csv_data:
        if line['Ingredients'] == 'No Reward':
            break
        names.append(f"{line['Ingredients']}")

for name in names:
    html_output += f'\n\t <li>{name}</li>'

print(html_output)
