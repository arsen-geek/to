import requests
import re
import pymorphy2
analyzer = pymorphy2.MorphAnalyzer()

def word2art(word, num = 1):
    lemma = normalize(word)
    article = ''
    for el in lemma:
        article += wiki_main(el, num) + '\n'
    return article

def normalize(word):
    parse_results = analyzer.parse(word)
    lemmata = []
    for result in parse_results:
        if result.normal_form not in lemmata:
            lemmata.append(result.normal_form)
    return lemmata

def wiki_main(lemma, num = 1): # если число -1, то выводятся абсолютно все значения
    if num == 0 or not isinstance(num, int): # если число равно 0, то выводится только лемма
        return lemma + '\n'
    r = requests.get('https://ru.wiktionary.org/wiki/' + lemma) # загрузка статьи
    if not r: # если такого слова на сайте нет, то выводится только лемма
        return lemma + '\n'
    if len(re.findall(r'<h1>', r.text)) > 1:
        rus = re.findall(r'id="Русский">Русский.+?<h1>', r.text, re.DOTALL)[0] # часть статьи про русский
    else:
        rus = r.text
    all_m = meanings(rus, num) # достаю по нужному количеству значений на омоним (в виде строк)
    m_txt = []
    for el in all_m:
        cut_exmpl = cut_ex(el) # отрезаю ненужное в строке
        m_txt.append(re.findall(r'(?<=>)[^<>]*?(?=<)', cut_exmpl)) # вырезаю слова
    return article(m_txt, lemma) # формирую статью

def txt_clean(text_0):
    text_1 = re.sub(r'&#\d{1,4};', ' ', text_0)
    text_1 = text_1.replace('( ', '')
    text_1 = text_1.replace(' )', '')
    text_1 = text_1.replace(r'. .', '.')
    text_1 = text_1.replace(r'..', '.')
    text_1 = text_1.replace(r'  ', ' ')
    text_1 = re.sub(r' (?=[.,?!:])', '', text_1)
    return text_1

def meanings(rus, num):
    meaning = re.findall(r'<h4>[^\n]+?Значение.+?(<ol><li>.+?</ol>)', rus, re.DOTALL) # статьи целиком на каждый омоним
    all_m = []
    for word in meaning:
        w_m = re.findall(r'<li>.+?</li>', word) # все определения на один омоним
        if len(w_m) > num and num != -1: # убираю лишние
            w_m_left = w_m[:num]
        else:
            w_m_left = w_m
        all_m.extend(w_m_left) # дополняю общий список
    return all_m

def cut_ex(el): # отрезаю ненужное
    cut = re.sub(r'(?<=<)span class.+', '', el) # отрезаю источники
    cut = re.sub(r'(?<=<)span style="font-size:smaller.+', '', cut) # отрезаю примеры
    cut = re.sub(r'(?<=<)sup id="cite_ref.+', '', cut) # отрезаю аннотации
    cut = re.sub(r'<[/]?.>', '', cut) # отрезаю проч.
    return(cut)

def article(m_txt, lemma):
    text = lemma + '\t' + 'https://ru.wiktionary.org/wiki/' + lemma + '\n'
    for i, el in enumerate(m_txt): # собираю текст
        text += '\t' + str(i+1) + '.' # нумерация слов
        for part in el:
            if part.strip(' '):
                if part.strip(' ')[0] != ',': # чтобы красиво запятая была
                    text += ' ' + part.strip(' ') 
                else:
                    text += part.strip(' ')
        text += '.\n'
    return txt_clean(text) # чищу финальный вариант текста
