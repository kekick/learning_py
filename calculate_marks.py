import os


def is_file_exists(file_path):
    return os.path.isfile(file_path)


def write_marks(file):
    try:
        lst = list(map(int, input().strip().split()))
        sem_marks = round(sum(lst) / len(lst), 1)
        if int(str(sem_marks)[2]) > 4:
            sem_marks = round(sem_marks + 0.1)
        okr = int(input("OKR: "))
        result = round(sem_marks + okr, 2) / 2
        NAME = input("Name: ")
        with open(f"{file}.txt", "a" if is_file_exists(f"{file}.txt") else "w", encoding="UTF-8 ") as marks:
            marks.write(f"{NAME}:   ОКР:{okr}   ЗА СЕМЕСТР:{sem_marks}   ИТОГ:{result} \n")
    except ValueError:
        print('Неверный ввод')


GROUPS = {
    "1k9191": 3,
    "2k9111": 20
}

update = input("Введите группу и количество людей(через пробел): ").split()
GROUPS.update({update[0]: int(update[1])})

while True:
    file = input("Группа: ")
    if file == '0':
        break
    if file in GROUPS:
        for i in range(GROUPS[file]):
            write_marks(file)
