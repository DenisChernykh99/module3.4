def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in str.lower(other_words[i]):
            same_words.append(other_words[i])
    return same_words
test_1 = single_root_words('Чин', 'Чиновник', 'чаша', 'поДчинение', 'ПочиНка', 'подключение')
test_2 = single_root_words('пер', 'ПерЕклЮчение', 'перЕвоД', 'ПроВод', 'ДениС', 'леТо')
print(test_1)
print(test_2)
