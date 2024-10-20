def single_root_words(root_word , *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        i = i.lower()
        if (root_word in i) or (i in root_word):
            same_words.append(i)

    print(same_words)
    return same_words

# def single_root_words(root_word , *other_words):
#     same_words = []
#     root_word = root_word.lower()
#     for i in other_words: # i: "Able"
#         i = i.lower() # i: "able" если i.lower(), а не i = i.lower(), то мы не сохраняем измен. значение, а создаём новое
#         if (root_word in i) or (i in root_word):
#             same_words.append(i)
#
#     print(same_words)
#     return same_words
#

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