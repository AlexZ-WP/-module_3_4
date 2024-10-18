def single_root_words(root_word , *other_words):
    same_words = []
    for i in other_words:

        i.lower()
        root_word.lower()
        if root_word in i or i in root_word:
            # i.upper()
            # root_word.upper()

            same_words.append(i)
    print(same_words)
    return same_words
    #если return на уровне if цикл заканчивается на первом совпадении
    # при таком располозении return цикл проходит по всему списку


    # print(other_words)
    #     print(*other_words)
    #     print(root_word,*other_words)
    #     print(type(other_words))
    #     print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

#if i <= root_word: при такой команде выдаёт:
# ['orichalcum', 'cheers']
# ['Able', 'Disable', 'Bagel'] не понятно почему для первого вызова вроде должен вообще ничего не выбратьъ
# для второго наоборот всё если сравнивается длина строки или ?
# if root_word in i or i in root_word: для такой конструкции получаем:
# ['richiest', 'orichalcum', 'richies']
# ['Disable']
#if root_word in i:для такой конструкции получаем:
# ['richiest', 'orichalcum', 'richies']
# []