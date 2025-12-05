class OpSystem():# Programm
    def __init__(self, name, systemID, size_gb, computerID):
        self.name = name
        self.size_gb = size_gb
        self.systemID = systemID
        self.computerID = computerID


class Computer():
    def __init__(self, computerID, model):
        self.computerID = computerID
        self.model = model


class OsComputer():
    def __init__(self, systemID, computerID):
        self.systemID = systemID
        self.computerID = computerID


opsystems = [
    OpSystem("Windows 10 Home", 1, 20, 1),
    OpSystem("Windows 10 Pro", 2, 27, 2),
    OpSystem("Windows 11", 3, 25, 3),
    OpSystem("MacOS Sonoma", 4, 28, 3),
    OpSystem("Arch Linux", 5, 1.3, 2)
]

computers = [
    Computer(1, "Рабочий компьютер IMac"),
    Computer(2, "Игровой компьютер ASUS"),
    Computer(3, "Офисный компьютер HP")
]

os_comp = [
    OsComputer(4, 1),
    OsComputer(2, 2),
    OsComputer(3, 2),
    OsComputer(5, 3),
    OsComputer(1, 3)
]


def counters(any_list, num_for_find):
    storage = 0
    for el in any_list:
        if el == num_for_find:
            storage += 1
    return storage


def finder_for_name(any_dict):
    name_result = dict()
    for item in any_dict:
        os_name = item[0]
        comp_model = item[1]
        if os_name[0].upper() == 'W':
            name_result[os_name] = comp_model
    return name_result


def filters(anything):
    for i in anything:
        return len(i.split()[0])


one_to_many_first = [
    (os.name, os.size_gb, comp.model)
    for os in opsystems
    for comp in computers
    if os.computerID == comp.computerID
]

one_to_many_twice = [
    (comp.model)
    for os in opsystems
    for comp in computers
    if os.computerID == comp.computerID
]

many_to_many_1 = [
    (os.name, pc.computerID)
    for os in opsystems
    for pc in os_comp
    if (os.computerID == pc.computerID) and (os.systemID == pc.systemID)
]


print("\n")
print("=" * 70)
print("Задание Б1 (Компьютеры со словом 'компьютер' и их операционные системы):")
print("=" * 70)
print("Сортировка по названиям операционных систем:")
print()

filtered_computers = [
    (os.name, os.size_gb, comp.model)
    for os in opsystems
    for comp in computers
    if os.computerID == comp.computerID and "компьютер" in comp.model.lower()
]

rez = sorted(filtered_computers)
for i in rez:
    print(f"Операционная система: {i[0]:<30} | Размер: {i[1]:>8} ГБ | Компьютер: {i[2]}")

print("\n")
print("=" * 70)
print("Задание Б2 (Компьютеры со средним размером операционных систем):")
print("=" * 70)
print("Отсортированы по среднему размеру ОС в ГБ:")
print()

comp_avg_size = dict()

for comp in computers:
    comp_os = [os.size_gb for os in opsystems if os.computerID == comp.computerID]
    if comp_os:
        avg_size = round(sum(comp_os) / len(comp_os), 2)
        comp_avg_size[comp.model] = avg_size

sorted_comp = sorted(list(comp_avg_size.items()), key=lambda x: x[1])

for computer, avg in sorted_comp:
    print(f"Компьютер: {computer:<35} | Средний размер ОС: {avg:>8.2f} ГБ")

print("\n")
print("=" * 70)
print("Задание Б3 (ОС, начинающиеся на 'W', и их компьютеры):")
print("=" * 70)
print("Сортировка по длине названия операционных систем:")
print()


many_w = [
    (os.name, comp.model)
    for os in opsystems
    for comp in computers
    if os.computerID == comp.computerID and os.name[0].upper() == 'W'
]

name_rez = sorted(many_w, key=lambda item: len(item[0].split()[0]))

for program in name_rez:
    print(f"ОС: {program[0]:<35} | Компьютер: {program[1]}")

print("\n")
print("=" * 70)
print("Конец выполнения программы")
print("=" * 70)