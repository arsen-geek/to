import csv
import word2art_normalize__wiki_main as p #импортирую две функции из файла word2art

#тут будут все медианные значения для 6 уровней, их легче сразу посчитать
alephA1 = 9708.2

#функция составляет словарь вида слово:его значение алеф
def level_dictionary(level):
    just_dict = {}
    filename = level + '.txt'
    with open('freqrnc2011.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            just_dict.update({row['Lemma']: float(row['Freq(ipm)'])*float(row['D'])})
    return just_dict

#на вход подаётся текст и уровень, выводятся слова, сложные для этого уровня
def hard_words_search(text, level):
    jd = level_dictionary(level)
    text = p.txt_clean(text)
    h_list = []
    for x in text.split():
        word = p.normalize(x)[0]
        try:
            if jd[word] <= alephA1 and not (word in h_list):
                h_list.append(word)
        except:
            pass
    return h_list


def HardWords(text, level):
    s = ''
    hard_words_list = hard_words_search(text, level)
    for word in hard_words_list:
        s += p.wiki_main(word)
        s += '\n'
    return s
