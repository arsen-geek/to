import re
import json
import word2art_normalize__wiki_main as p #импортирую две функции из файла word2art

#тут будут все медианные значения для 6 уровней, их легче сразу посчитать
level2aleph = {
    'A1': 9708.2, 
    'A2': 0,
    'B1': 0,
    'B2': 0,
    'C1': 0,
    'C2': 0
}

#на вход подаётся текст и уровень, выводятся слова, сложные для этого уровня
def hard_words_search(text, level):
    with open('aleph.json', encoding='utf-8') as f:
        jd = json.load(f)
    h_list = []
    for x in text.split():
        word_clean = re.findall(r'[А-яЁё-]+', x)
        if not word_clean:
            continue
        word = p.normalize(word_clean[0])[0]
        try:
            if jd[word] <= level2aleph[level] and not (word in h_list) and not p.is_POS_bad(word)::
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
