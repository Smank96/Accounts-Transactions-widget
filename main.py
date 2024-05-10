from utils import load_data, mask_number, delete_canceled_operations, sort_list_by_date
from Operation import Operation


def main():
    # загружаем список операций
    raw_operations = load_data()
    operations = []

    for value in raw_operations:
        # создание экземпляра класса Operation.
        operation = Operation(operation_id=value.get('id'),
                              state=value.get('state'),
                              date=value.get('date'),
                              operation_amount=value.get('operationAmount'),
                              description=value.get('description'),
                              destination=value.get('to'),
                              remitter=value.get('from')
                              )

        # форматирование даты.
        Operation.formate_date(operation)

        # маскировка счета/карты получателя.
        operation.destination = mask_number(str(operation.destination))

        # маскировка счета/карты отправителя.
        operation.remitter = mask_number(str(operation.remitter))

        # добавление экземпляра класса Operation в список.
        operations.append(operation)

    # удаление отмененных операций из списка.
    operations = delete_canceled_operations(operations)

    # сортировка списка выполненных операций по дате.
    operations = sort_list_by_date(operations)

    # вывод на печать 5 последних операций.
    for i in range(5):
        print(operations[i], "\n")


main()
