from random import sample


def failist_to_dict(f):
    dictionary = {}
    try:
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('-')
                if len(parts) == 2:
                    word, translation = parts
                    dictionary[word.strip()] = translation.strip()
    except FileNotFoundError:
        print("Файл", f, "не найден.")
    return dictionary

def add_word(dictionary, word, translation):
    dictionary[word] = translation # word = key, translation= meaning
    print("Слово успешно добавлено в словарь.")

def edit_word(dictionary, word, new_translation): #Ищет слово с всловаре и если его нет выводит сообщение о отсутствии
    if word in dictionary:
        dictionary[word] = new_translation
        print("Перевод слова успешно отредактирован.")
    else:
        print("Слово не найдено в словаре.")

def remove_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        print("Слово успешно удалено из словаря.") # если слово найдено
    else:
        print("Слово не найдено в словаре.") # если слово не найдено

def translate(dictionary, word):
    if word in dictionary:
        print(word + ": " + dictionary[word]) # выводит слово и перевод через двоеточие
    else:
        print("Слово не найдено в словаре.") # если слово не найдено

def test_knowledge(dictionary):
    score = 0
    total_words = min(len(dictionary), 5) if dictionary else 0 # проверяет кол-во слов, если меньше 5 спрашивает сколько есть
    if total_words == 0:
        print("Словарь пустой. Невозможно провести тест.")
        return

    words_to_test = sample(list(dictionary.keys()), total_words) #Преобразует представление ключей в список, чтобы его можно было использовать с функцией sample.
    for word in words_to_test:
        print("Переведите слово '" + word + "':") # выбирает слово из словаря 
        answer = input().strip()
        if answer.lower() == dictionary[word].lower():
            print("Правильно!") # если правильно увеличивает счет на 1 
            score += 1
        else:
            print("Неправильно. Правильный перевод: " + dictionary[word]) #выводит правильный перевод из словаря
    print("Вы получили {}/{} баллов. ({:.2f}%)".format(score, total_words, (score / total_words) * 100))
