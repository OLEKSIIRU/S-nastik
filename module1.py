from random import *
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
        print(f"Файл {f} не найден.")
    return dictionary

def add_word(dictionary, word, translation):
    dictionary[word] = translation
    print("Слово успешно добавлено в словарь.")

def edit_word(dictionary, word, new_translation):
    if word in dictionary:
        dictionary[word] = new_translation
        print("Перевод слова успешно отредактирован.")
    else:
        print("Слово не найдено в словаре.")

def remove_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        print("Слово успешно удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def translate(dictionary, word):
    if word in dictionary:
        print(f"{word}: {dictionary[word]}")
    else:
        print("Слово не найдено в словаре.")

def test_knowledge(dictionary):
    score = 0
    total_words = min(len(dictionary), 5) if dictionary else 0
    if total_words == 0:
        print("Словарь пустой. Невозможно провести тест.")
        return

    words_to_test = sample(list(dictionary.keys()), total_words)
    for word in words_to_test:
        print(f"Переведите слово '{word}':")
        answer = input().strip()
        if answer.lower() == dictionary[word].lower():
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильный перевод: {dictionary[word]}")
    print(f"Вы получили {score}/{total_words} баллов. ({(score / total_words) * 100:.2f}%)")



