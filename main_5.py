# Чтение слов из файла
with open('words.txt', 'r', encoding='utf-8') as file:
    words = [word.strip() for word in file]

# Функция для поиска сцепленных слов
def find_concatenated_words(input_word, words_list):
    concatenated_words = []
    for word in words_list:
        if input_word != word:
            if input_word.endswith(word[:2]):
                concatenated_words.append(input_word + word[2:])
            if input_word.startswith(word[-2:]):
                concatenated_words.append(word + input_word[2:])
    return concatenated_words

# Основной цикл программы
while True:
    user_input = input("Введите первое слово: ")
    if user_input == "exit":
        break
    concatenated = find_concatenated_words(user_input, words)
    print("Программа выводит:")
    for word in concatenated:
        print(word)