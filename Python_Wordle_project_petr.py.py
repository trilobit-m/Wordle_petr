import random

ANSI_GREEN = '\033[92m'
ANSI_YELLOW = '\033[93m'
ANSI_NORMAL = '\033[0m'

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

flag = True
slova = ["гривна", "изотоп", "буртит", "зигзаг", "цезарь",
         "бархат", "анчоус", "эпопея", "карбон", "вулкан",
         "кивок", "винил", "кольт", "гнида", "аорта",
         "занос", "алтын", "иудей", "морда", "юнкер",
         "позор", "камео", "спрос", "лавка", "бабка",
         "дурка", "дубок", "окно", "фора", "уезд"]
count = 0
vivod = list()

# Глобальные переменные

slovo = random.choice(slova)
slova.remove(slovo)

# Первое слово

while ((a := input()).lower) != slovo or count < 6:
    count += 1  # Счётчик попыток
    print(bold_text(f"Длина слова равна {len(slovo)} буквам"))
    
    
    if a == "/restart":
        slovo = random.choice(slova)
        slova.remove(slovo)
        print(bold_text("Попробуйте снова!"))   # Команда перезапуска


    elif a == "/pass":
        flag = False
        break   # Команда сдаться


    elif a == "/help":
        print("Загадано слово. У вас есть 6 попыток. Нажмите кнопку ВВОД, чтобы отправить.")
        print("После каждой попытки цвет фона под буквами будет меняться, чтобы показать, насколько ваше предположение было близко к загаданному слову:")
        print("-Зелёный цвет буквы означает что буква стоит на своём месте.")
        print("-Жёлтый цвет буквы означает, что буква есть в слове, но соит не на своём месте.")
        print()
        print("Список возможных команд:")
        print()
        print("+ /help - получить помощь")
        print("+ /pass - сдаться")
        print("+ /restart - перезапуск")
        print("+ /")    # Команда помощь


    elif len(a) != len(slovo) or not a.isalpha():
        print(bold_text("Слово не подходит!"))    # Проверка слова


    else:
        a1 = a.split("")
        slovo1 = slovo.split("")
        
        slovo_bukvi = slovo1.copy()

        for i in range(len(slovo)):
            if a1[i] == slovo1[i]:
                vivod.append(ANSI_GREEN, a1[i], ANSI_NORMAL)
            elif a1[i] in slovo_bukvi:
                slovo_bukvi.remove(a1[i])
                vivod.append(ANSI_YELLOW, a1[i], ANSI_NORMAL)
            else:
                vivod.append(a1[i])
    print(vivod)
if flag and count <= 6:
    print("Поздравляю, вы победили!")
else:
    print("К сожалению у вас не получилось победить.")

# Вывод сообщения о победе