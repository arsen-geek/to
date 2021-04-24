# напечатать леммы, у которых D больше x

import csv
# Lemma, PoS, Freq(ipm)
with open('freqrnc2011.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = '\t')
    for row in reader:
        d = float(row['D'])
        
        x = 98
        
        if (d > x):
            print(row['Lemma'])