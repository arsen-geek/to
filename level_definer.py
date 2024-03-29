from statistics import median
import csv

alephA1 = 97.082
# alephA2 = ?
# alephB1= ?
# alephB2 = ?
# alephC1 = ?
alephC2 = 1.7955

#функция составляет словарь заданного уровня
def level_dictionary(level):
    level_words = []
    level_dict = {}
    filename = level + '.txt'
    with open(filename, encoding='utf-8') as file:
        for line in file:
            level_words.append(line.split()[0])
    with open('freqrnc2011.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '\t')
        for row in reader:
            if row['Lemma'] in level_words:
                level_dict.update({row['Lemma'] : float(row['Freq(ipm)'])*float(row['D']) / 100 })
                level_words.remove(row['Lemma'])
    return (median(level_dict.values()))
