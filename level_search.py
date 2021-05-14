import re
import json
import word2art_normalize__wiki_main as p #импортирую две функции из файла word2art

# пороговые значения для уровней
level2aleph = {
    'A1': 97.082,
    'A2': 92,
    'B1': 85,
    'B2': 67,
    'C1': 20,
    'C2': 1.7955
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
            if jd[word] <= level2aleph[level] and not (word in h_list) and not p.is_POS_bad(word):
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
