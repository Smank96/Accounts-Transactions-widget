from utils import mask_account_number, mask_card_number, delete_canceled_operations, sort_list_by_date, mask_number
from Operation import Operation


def test_mask_account_number():
    assert mask_account_number("Счет 64686473678894779589") == "Счет **9589"


def test_mask_card_number():
    assert mask_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_number():
    assert mask_number("Счет 11776614605963066702") == "Счет **6702"
    assert mask_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_delete_canceled_operations():
    operations = []

    executed_operation = Operation(operation_id=441945886,
                                   state="EXECUTED",
                                   date="2019-08-26T10:50:58.294041",
                                   operation_amount="123",
                                   description="Перевод организации",
                                   destination="Maestro 1596837868705199",
                                   remitter="Счет 64686473678894779589",
                                   )

    operations.append(executed_operation)

    canceled_operation = Operation(operation_id=594226727,
                                   state="CANCELED",
                                   date="2018-09-12T21:27:25.241689",
                                   operation_amount="123",
                                   description="Перевод организации",
                                   destination="Visa Platinum 1246377376343588",
                                   remitter="Счет 14211924144426031657",
                                   )

    operations.append(canceled_operation)

    executed_operations = delete_canceled_operations(operations)

    assert len(executed_operations) == 1


def test_sort_list_by_date():
    operations = []

    operation1 = Operation(operation_id=441945886,
                           state="EXECUTED",
                           date="2019-08-26T10:50:58.294041",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation1)
    operations.append(operation1)

    operation2 = Operation(operation_id=594226727,
                           state="CANCELED",
                           date="2018-09-12T21:27:25.241689",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation2)
    operations.append(operation2)

    operation3 = Operation(operation_id=41428829,
                           state="EXECUTED",
                           date="2019-07-03T18:35:29.512364",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation3)
    operations.append(operation3)

    operation4 = Operation(operation_id=939719570,
                           state="CANCELED",
                           date="2018-06-30T02:08:58.425572",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation4)
    operations.append(operation4)

    operation5 = Operation(operation_id=587085106,
                           state="CANCELED",
                           date="2018-03-23T10:45:06.972075",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation5)
    operations.append(operation5)

    sorted_list = sort_list_by_date(operations)

    assert sorted_list[0] == operation1
    assert sorted_list[1] == operation3
    assert sorted_list[2] == operation2
    assert sorted_list[3] == operation4
    assert sorted_list[4] == operation5


def test_formate_date():

    operation1 = Operation(operation_id=441945886,
                           state="EXECUTED",
                           date="2019-08-26T10:50:58.294041",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation1)

    operation2 = Operation(operation_id=594226727,
                           state="CANCELED",
                           date="2018-09-12T21:27:25.241689",
                           operation_amount=" ",
                           description=" ",
                           destination=" ",
                           remitter=" ",
                           )

    Operation.formate_date(operation2)

    assert operation1.date == "26.08.2019"
    assert operation2.date == "12.09.2018"
