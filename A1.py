import csv

# список слов для уровня А1 (выкачать из файла)
words_A1 = []

with open('a1.txt') as file:
    for line in file:
        words_A1.append(line.split()[0])

# создать словарь -слово из words_A1- : -ipm-
A1_with_ipm = {}

with open('freqrnc2011.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = '\t')
    for row in reader:
        if row['Lemma'] in words_A1:
            A1_with_ipm.update({row['Lemma'] : float(row['Freq(ipm)'])})
            words_A1.remove(row['Lemma'])


# медиана ipm для A1
from statistics import median

print(median(A1_with_ipm.values()))