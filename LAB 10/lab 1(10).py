import csv


data = [
    ['Name', 'Age', 'City'],
    ['kenil', 23, 'surat'],
    ['jenil', 30, 'bangluru'],
    ['viraj', 28, 'Delhi']
]


with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully!")