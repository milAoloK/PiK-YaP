from dataclasses import dataclass
from typing import Iterable, List, Dict, Tuple


@dataclass(frozen=True)
class OpSystem:
    name: str
    system_id: int
    size_gb: float
    computer_id: int


@dataclass(frozen=True)
class Computer:
    computer_id: int
    model: str


@dataclass(frozen=True)
class OsComputer:
    system_id: int
    computer_id: int


def build_default_data() -> tuple[list[OpSystem], list[Computer], list[OsComputer]]:

    opsystems = [
        OpSystem("Windows 10 Home", 1, 20, 1),
        OpSystem("Windows 10 Pro", 2, 27, 2),
        OpSystem("Windows 11", 3, 25, 3),
        OpSystem("MacOS Sonoma", 4, 28, 3),
        OpSystem("Arch Linux", 5, 1.3, 2),
    ]

    computers = [
        Computer(1, "Рабочий компьютер IMac"),
        Computer(2, "Игровой компьютер ASUS"),
        Computer(3, "Офисный компьютер HP"),
    ]

    os_comp = [
        OsComputer(4, 1),
        OsComputer(2, 2),
        OsComputer(3, 2),
        OsComputer(5, 3),
        OsComputer(1, 3),
    ]
    return opsystems, computers, os_comp


# ----------------------------
# Task B1
# ----------------------------

def task_b1_filtered_computers(
    opsystems: Iterable[OpSystem],
    computers: Iterable[Computer],
    keyword: str = "компьютер",
) -> list[tuple[str, float, str]]:
   
    kw = keyword.lower()
    comp_by_id = {c.computer_id: c for c in computers}

    filtered: list[tuple[str, float, str]] = []
    for os in opsystems:
        comp = comp_by_id.get(os.computer_id)
        if comp and kw in comp.model.lower():
            filtered.append((os.name, os.size_gb, comp.model))

    return sorted(filtered)


# ----------------------------
# Task B2
# ----------------------------

def task_b2_average_os_size_by_computer(
    opsystems: Iterable[OpSystem],
    computers: Iterable[Computer],
    *,
    rounding: int = 2,
) -> list[tuple[str, float]]:

    sizes_by_comp: Dict[int, list[float]] = {}
    for os in opsystems:
        sizes_by_comp.setdefault(os.computer_id, []).append(float(os.size_gb))

    result: list[tuple[str, float]] = []
    for comp in computers:
        sizes = sizes_by_comp.get(comp.computer_id, [])
        if sizes:
            avg = round(sum(sizes) / len(sizes), rounding)
            result.append((comp.model, avg))

    return sorted(result, key=lambda x: x[1])


# ----------------------------
# Task B3 
# ----------------------------

def _first_word_len(s: str) -> int:
    first = s.split()[0] if s.split() else ""
    return len(first)


def task_b3_windows_os_and_computers(
    opsystems: Iterable[OpSystem],
    computers: Iterable[Computer],
) -> list[tuple[str, str]]:
    
    comp_by_id = {c.computer_id: c for c in computers}

    pairs: list[tuple[str, str]] = []
    for os in opsystems:
        if os.name and os.name[0].upper() == "W":
            comp = comp_by_id.get(os.computer_id)
            if comp:
                pairs.append((os.name, comp.model))

    return sorted(pairs, key=lambda item: _first_word_len(item[0]))



def main() -> None:
    opsystems, computers, _ = build_default_data()

    print("\n" + "=" * 70)
    print("Задание Б1 (Компьютеры со словом 'компьютер' и их операционные системы):")
    print("=" * 70)
    print("Сортировка по названиям операционных систем:\n")

    for os_name, size_gb, comp_model in task_b1_filtered_computers(opsystems, computers):
        print(f"Операционная система: {os_name:<30} | Размер: {size_gb:>8} ГБ | Компьютер: {comp_model}")

    print("\n" + "=" * 70)
    print("Задание Б2 (Компьютеры со средним размером операционных систем):")
    print("=" * 70)
    print("Отсортированы по среднему размеру ОС в ГБ:\n")

    for comp_model, avg in task_b2_average_os_size_by_computer(opsystems, computers):
        print(f"Компьютер: {comp_model:<35} | Средний размер ОС: {avg:>8.2f} ГБ")

    print("\n" + "=" * 70)
    print("Задание Б3 (ОС, начинающиеся на 'W', и их компьютеры):")
    print("=" * 70)
    print("Сортировка по длине названия операционных систем:\n")

    for os_name, comp_model in task_b3_windows_os_and_computers(opsystems, computers):
        print(f"ОС: {os_name:<35} | Компьютер: {comp_model}")

    print("\n" + "=" * 70)
    print("Конец выполнения программы")
    print("=" * 70)


if __name__ == "__main__":
    main()
