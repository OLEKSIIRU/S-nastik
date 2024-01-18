
def loe_failist(f):
    with open(f, 'r', encoding='utf-8') as fail:
        return [rida.strip() for rida in fail]

def loo_tõlked(r_list, e_list):
    return {r: e for r, e in zip(r_list, e_list)}

def lisa_sõna(word, t_dict, new_trans):
    t_dict.setdefault(word, new_trans)

def tõlgi_sõna(word, t_dict):
    return t_dict.get(word, "Перевод не найден")


rus = loe_failist("rus.txt") # Загрузка списков слов
est = loe_failist("est.txt")


trans_dict = loo_tõlked(rus, est) # Создание словаря для перевода


user_word = input("Введите слово для перевода: ")# Запрос пользователя


if user_word in trans_dict:
    translated_word = tõlgi_sõna(user_word, trans_dict)
    print(f"Перевод слова '{user_word}': {translated_word}")   # Проверка, есть ли слово в словаре
else:
 
    user_translation = input("Перевод для '{user_word}' не найден. Введите перевод: ")      # Запрос перевода и добавление в словарь
    lisa_sõna(user_word, trans_dict, user_translation)
    print("Слово '{user_word}' добавлено в словарь с переводом '{user_translation}'")


print(trans_dict)   # Печать обновленного словаря





























#def loe_failist(f):
#    with open(f, 'r', encoding='utf-8') as fail:
#        return [rida.strip() for rida in fail]

#def loo(rus_list, est_list):
#    return {rus: est for rus, est in zip(rus_list, est_list)}

#def translate(word, trans_dict):
#    return trans_dict.get(word, "Перевод не найден")


#rus = loe_failist("rus.txt")
#est = loe_failist("est.txt")


#trans_dict = loo(rus, est)


#word_to_translate = "привет"
#translated_word = translate(word_to_translate, trans_dict)
#print(f"Перевод слова '{word_to_translate}': {translated_word}")

