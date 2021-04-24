# напечатать леммы, которые не междометия или им. собств., с imp больше x

import csv

# Теги:
# Lemma, PoS, Freq(ipm), D

with open('freqrnc2011.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = '\t')
    for row in reader:
        ipm = float(row['Freq(ipm)'])
        
        x = 100
        
        if (ipm > x) and (row['PoS'] != 'intj') and ('.PROP' not in row['PoS']):
            print(row['Lemma'])