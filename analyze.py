from collections import Counter
from string import punctuation

alph = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
filename = input("Дайте будь-ласка назву файлу (без txt) ") + ".txt"
#filesize = getsize(filename)
file = open(filename, "r", encoding="utf-8")
text = file.read().strip().translate(str.maketrans('', '', punctuation)).lower().replace("—", "").replace("«", "").replace("»", "")
file.close()
count = Counter(text)
print("В алфавітному порядку")
for k in sorted(count.keys()):
    if not k.isspace():
           print(f"{k}: {count[k] / len(text)}")
print("В частотному порядку")
for k in sorted(count, key=count.get, reverse=True):
    if not k.isspace():
           print(f"{k}: {count[k] / len(text)}")
print("послідовність літер")
for k in sorted(count, key=count.get, reverse=True):
    if not k.isspace():
        print(f"{k}", end = '')
text = text.replace(" ", "")
tokens = [token for token in text]
bigrams = zip(*[tokens[0:], tokens[1:]])
count_bi = Counter(bigrams)
#print()
#print(count_bi['в', 'а'])
#print(sum(count_bi.values()))
print("\n "+alph)
for first_lettter in alph:
    print(first_lettter, end = '')
    for second_letter in alph:
        #probability = count_bi[first_lettter, second_letter]/(len(alph)*len(alph))
        step = max(count_bi.values())/5
        value = count_bi[first_lettter, second_letter]
        if (value==0):
            print(" ", end = '')
        if (value<step and value>0):
            print("░", end = '')
        if (value > step and value < step*2):
            print("▒", end='')
        if (value > step*2 and value < step*3):
            print("▓", end='')
        if (value > step*3 and value < step*4):
            print("█", end='')
        if (value>step*4):
            print("╬", end='')
    print()
print("Частоти біграм")
i = 1
for k in sorted(count_bi, key=count_bi.get, reverse=True):
    print(f"{i}: {k}: {count_bi[k] / (len(alph)*len(alph))}")
    i = i + 1
    if (i == 31): break
trigrams = zip(*[tokens[0:], tokens[1:], tokens[2:]])
count_tri = Counter(trigrams)
i = 0
print("Частоти триграм")
for k in sorted(count_tri, key=count_tri.get, reverse=True):
    print(f"{i}: {k}: {count_tri[k] / (len(alph)*len(alph)*len(alph))}")
    i = i + 1
    if (i == 31): break
#print([''.join(bigram) for bigram in bigrams])
#print([''.join(trigram) for trigram in trigrams])
#for k in count.keys():
#    if not k.isspace():
#        print(f"{k}: {count[k] / len(text)}")
#    else:
#        print(f"U+{format(ord(k), 'x')}: {count[k] / len(text)}")
input()