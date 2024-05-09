import json
from datetime import datetime


def load_data() -> list[dict]:
    """
    Возвращает список операций из файла json.
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


def mask_number(raw_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Видны первые 6 цифр и последние 4, разбито блоками по 4 цифры, разделенных пробелом.
    ------------------------------
    Маскирует номер счета в **XXXX.
    Видны только последние 4 цифры номера счета.
    """
    if raw_number[:4] == "Счет":
        raw_account_number = raw_number[6:]
        masked_account_number = "**" + raw_account_number[-4:]

        return "Счет " + masked_account_number
    else:
        card_number = ""
        for i in raw_number:
            try:
                num = int(i)
                card_number += str(num)
            except ValueError:
                continue

        masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

        split_number = raw_number.split()

        if len(split_number) == 2:
            return str(split_number[0]) + " " + masked_card_number
        elif len(split_number) == 3:
            return str(split_number[0]) + " " + str(split_number[1]) + " " + masked_card_number


def delete_canceled_operations(canceled_operations: list) -> list:
    """
    Принимает список в качестве аргумента.
    Удаление операций из списка со статусом "CANCELED".
    Возвращает список операций со статусом "EXECUTED".
    """
    executed_operations = []

    for operation in canceled_operations:
        if operation.state == "EXECUTED":
            executed_operations.append(operation)

    return executed_operations


def sort_list_by_date(unsorted_list: list) -> list:
    """
    Принимает список в качестве аргумента.
    Сортирует список по дате.
    Возвращает отсортированный список.
    """
    sorted_list = sorted(unsorted_list,
                         key=lambda operation: datetime.strptime(operation.date, "%d.%m.%Y").date(),
                         reverse=True)

    return sorted_list
