from random import choice

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []

words = ("code", "bit", "list", "soul", "next")


def morse_encode(word):
    """
    Переводит слово из букв в морзянку
    """
    print(" ".join([morse_code[letter] for letter in word]))


def get_word(words):
    """
    Вытаскивает псевдослучайное слово из списка слов
    """
    return choice(words)


def print_statistics(answers):
    """
    Подсчитывает и выводит статистику правельных
    и неправельных ответов
    """
    true_answer = 0
    false_answer = 0
    for answer in answers:
        if answer is True:
            true_answer += 1
        elif answer is False:
            false_answer += 1
    print(f"Всего задачек: {len(answers)}\n"
          f"Отвечено верно: {answers.count(True)}\n"
          f"Отвечено неверно: {answers.count(False)}\n")


print("Сегодня мы потренируемся расшифровывать морзянку.")
input("Нажмите Enter и начнем")

i = 1
while i < 6:
    print(f"Слово {i}")

    random_word = get_word(words)
    morse_word = morse_encode(random_word)

    answer = input("\nВпишите слово на английском языке: ")

    if answer == random_word:
        answers.append(True)
        print("Молодец. Ответ правельный.\n")
    else:
        answers.append(False)
        print("К сожалению, ответ неверный.\n")
    i += 1

print_statistics(answers)
