from Transaction import Transaction
from Process import Process


class Debt(Process):
    _currency_list = ['usd', 'ru', 'euro', 'riel']

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.currency_list = ['usd', 'ru', 'euro', 'riel']
        self.debt_currency = "usd"
        self.debt_amount = 0
        self._able.update({'CHANGE_CURRENCY': self.change_currency, 'GIVE': self.give, 'TAKE': self.take})

    def get_button_name(self):
        return self.related_processes[0].name + "'s debt: " + str(self.debt_amount) + ' ' + str(self.debt_currency)

    def change_currency(self, text, date: float, init: bool):
        currency = text.split(' ')[1]
        if currency not in Debt._currency_list:
            raise ValueError('Value should be positive integer number')
        elif self.debt_amount != 0:
            raise ValueError('Can not change currency when debt is not zero')
        self.add_transaction(Transaction(date, f'CHANGE_NAME {currency} from {self.debt_currency}', True), init)
        self.debt_currency = currency

    def give(self, text, date: float, init: bool):
        amount = text.split(' ')[1]
        try:
            amount = int(amount)
        except Exception:
            raise ValueError('Value should be positive integer number')
        if amount < 0:
            raise ValueError('Value should be positive integer number')
        self.add_transaction(Transaction(date, f'GIVE {amount} from debt {self.debt_amount}', True), init)
        self.debt_amount -= amount

    def take(self, text, date: float, init: bool):
        amount = text.split(' ')[1]
        try:
            amount = int(amount)
        except Exception:
            raise ValueError('Value should be positive integer number')
        if amount < 0:
            raise ValueError('Value should be positive integer number')
        self.add_transaction(Transaction(date, f'TAKE {amount} from debt {self.debt_amount}', True), init)
        self.debt_amount += amount



