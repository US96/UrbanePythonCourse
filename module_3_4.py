def single_root_words(root_word, *other_words):
    # Создаем пустой список, в который будем добавлять подходящие слова
    same_words = []
    
    # Приводим root_word к нижнему регистру для сравнения без учета регистра
    root_word_lower = root_word.lower()
    
    # Перебираем все слова, переданные в *other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        
        # Проверяем, содержится ли root_word в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если условие выполнено, добавляем слово в список
            same_words.append(word)
    
    # Возвращаем список найденных слов
    return same_words

# Вызов функции с тестовыми примерами
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на экран
print(result1)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']
