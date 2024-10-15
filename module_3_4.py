def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для сравнения
    root_word = root_word.lower()
    
    # Пустой список для подходящих слов
    same_words = []
    
    # Перебираем остальные слова
    for word in other_words:
        # Приводим каждое слово к нижнему регистру и проверяем наличие root_word
        if root_word in word.lower() or word.lower() in root_word:
            same_words.append(word)
    
    # Возвращаем список подходящих слов
    return same_words

# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата на консоль
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
