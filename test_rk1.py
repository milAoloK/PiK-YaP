import pytest

from rk1_refactored import (
    build_default_data,
    task_b1_filtered_computers,
    task_b2_average_os_size_by_computer,
    task_b3_windows_os_and_computers,
)


def test_b1_filters_by_keyword_and_sorts():
    opsystems, computers, _ = build_default_data()
    result = task_b1_filtered_computers(opsystems, computers, keyword="компьютер")

# где содержится слово компьютер
    assert len(result) == 5

    # отсортированы по алфовиту, потом вторично по размеру
    assert [r[0] for r in result] == [
        "Arch Linux",
        "MacOS Sonoma",
        "Windows 10 Home",
        "Windows 10 Pro",
        "Windows 11",
    ]


def test_b2_computes_average_sizes_and_sorts_by_average():
    opsystems, computers, _ = build_default_data()
    result = task_b2_average_os_size_by_computer(opsystems, computers)


    # comp1: 20
    # comp2: (27 + 1.3)/2 = 14.15
    # comp3: (25 + 28)/2 = 26.5
    assert result == [
        ("Игровой компьютер ASUS", 14.15),
        ("Рабочий компьютер IMac", 20.0),
        ("Офисный компьютер HP", 26.5),
    ]


def test_b3_returns_only_windows_and_sorts_by_first_word_length():
    opsystems, computers, _ = build_default_data()
    result = task_b3_windows_os_and_computers(opsystems, computers)

    # Начинаются с W
    assert [r[0] for r in result] == ["Windows 10 Home", "Windows 10 Pro", "Windows 11"]

    # отсортированы по слову "Windows"
    assert result[0][1] == "Рабочий компьютер IMac"
    assert result[1][1] == "Игровой компьютер ASUS"
    assert result[2][1] == "Офисный компьютер HP"
