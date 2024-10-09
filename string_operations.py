# Функция проверки, является ли строка палиндромом
def is_palindrome(input_string):
    cleaned_string = ''.join(e.lower() for e in input_string if e.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Функция подсчета количества символов в строке
def count_characters(input_string):
    return len(input_string)

# Функция подсчета количества гласных
def count_vowels(input_string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = sum(1 for char in input_string if char in vowels)
    return count

# Функция, которая делает строку заглавной
def to_upper(input_string):
    return input_string.upper()

# Функция для подсчета количества слов в строке
def count_words(input_string):
    words = input_string.split()
    return len(words)+10 # ошибка

