#  * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
#  ценность. В случае с английским алфавитом очки распределяются
#  так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
#  B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков;
#  J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются
#  так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
#  Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
#  Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного
#  пользователем слова. Будем считать, что на вход подается только одно слово,
#  которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

eng_letter = {
    1:'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}
russian_letter ={
1:'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}
N= abs(int(input('Введите цифру 1 если слова на английском языке, 2 если на русском языке')))
word = input('Введите слово: ').upper()
if N == 1:
    print (f'За слово {word} Вы получаете', sum([k for i in word for k, v in eng_letter.items() if i in v]), 'очков')
elif N == 2:
    print(f'За слово {word} вы получаете', sum([k for i in word for k, v in russian_letter.items() if i in v]), 'очков')
else:
    print('Вы не правильно ввели слово!')