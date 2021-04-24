# поиск строки в словаре по лемме

import csv

with open('freqrnc2011.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = '\t')
    for row in reader:
        if row['Lemma'] == 'елка':
            print(row)