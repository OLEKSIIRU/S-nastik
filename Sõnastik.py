
from module1 import failist_to_dict, translate, add_word, edit_word, remove_word, test_knowledge
def main():
    rus_dict = failist_to_dict('rus.txt')
    est_dict = failist_to_dict('est.txt')
    print("Словарь с русского на эстонский:", rus_dict)
    print("Словарь с эстонского на русский:", est_dict)

    while True:
        print("\nМеню:")
        print("1: Перевод слова")
        print("2: Добавить слово в словарь")
        print("3: Редактировать перевод слова")
        print("4: Удалить слово из словаря")
        print("5: Проверить знание слов")
        print("0: Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            language = input("Выберите язык (rus/est): ")
            if language.lower() == "rus":
                word = input("Введите слово: ")
                translate(rus_dict, word)
            elif language.lower() == "est":
                word = input("Sissetage sõna: ")
                translate(est_dict, word)
            else:
                print("Неверный выбор языка.")
        elif choice == "2":
            language = input("Выберите язык (rus/est): ")
            word = input("Введите слово: ")
            translation = input("Введите перевод: ")
            if language.lower() == "rus":
                add_word(rus_dict, word, translation)
            elif language.lower() == "est":
                add_word(est_dict, word, translation)
            else:
                print("Неверный выбор языка.")
        elif choice == "3":
            language = input("Выберите язык (rus/est): ")
            word = input("Введите слово: ")
            new_translation = input("Введите новый перевод: ")
            if language.lower() == "rus":
                edit_word(rus_dict, word, new_translation)
            elif language.lower() == "est":
                edit_word(est_dict, word, new_translation)
            else:
                print("Неверный выбор языка.")
        elif choice == "4":
            language = input("Выберите язык (rus/est): ")
            word = input("Введите слово: ")
            if language.lower() == "rus":
                remove_word(rus_dict, word)
            elif language.lower() == "est":
                remove_word(est_dict, word)
            else:
                print("Неверный выбор языка.")
        elif choice == "5":
            test_language = input("Выберите язык для тестирования (rus/est): ")
            if test_language.lower() == "rus":
                test_knowledge(rus_dict)
            elif test_language.lower() == "est":
                test_knowledge(est_dict)
            else:
                print("Неверный выбор языка.")
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()