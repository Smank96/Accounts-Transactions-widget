from datetime import datetime


class Operation:
    """
    Описывает операцию перевода и её аттрибуты.
    """
    def __init__(self,
                 operation_id,
                 state,
                 date,
                 operation_amount,
                 description,
                 destination,
                 remitter=None
                 ):

        self.operation_id = operation_id
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.destination = destination
        self.remitter = remitter

    def __str__(self):
        string1 = f"{self.date} {self.description}"

        # проверка на наличие отправителя платежа(from).
        if self.remitter:
            self.remitter += " -> "
        else:
            self.remitter = ""

        string2 = f"{self.remitter}{self.destination}"
        string3 = f"{self.operation_amount.get("amount")} {self.operation_amount.get("currency").get("name")}"

        return f"{string1}\n{string2}\n{string3}"

    def formate_date(self):
        """
        Принимает экземпляр класса в качестве аргумента.
        Форматирует дату в формате ДД.ММ.ГГГГ, в переданном экземпляре класса.
        """
        if self.date:
            raw_date = self.date
            raw_date = raw_date[0:10]
            date = datetime.strptime(raw_date, '%Y-%m-%d').date()

            self.date = date.strftime('%d.%m.%Y')
