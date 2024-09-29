import datetime
from Transaction import Transaction
from Process import Process


class Debt(Process):
    _currency_list = ['usd', 'ru', 'euro', 'riel']

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.currency_list = ['usd', 'ru', 'euro', 'riel']
        self.debt_currency = "usd"
        self.debt_amount = 0
        self.additional_ables = {'CHANGE_CURRENCY': self.change_currency, 'GIVE': self.give, 'TAKE': self.take}
        self._able.update(self.additional_ables)

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

    def get_all_transaction(self):
        ans = []
        for transaction in reversed(self.get_data()):
            if transaction.official:
                date = datetime.datetime.fromtimestamp(transaction.date)
                date_text = date.strftime("%Y-%m-%d %H:%M:%S")
                tag = transaction.text.split()[0]
                if tag == 'INFO':
                    tag2 = transaction.text.split()[1]
                    if tag2 == 'New':
                        message = f'{date_text}\nThe process was created'
                    elif tag2 == 'CROSS':
                        message = f'{date_text}\nThe process was crossed'
                    else:
                        message = f'{date_text}\nSome another information'
                elif tag == 'CROSS':
                    message = f'{date_text}\nThe process was crossed'
                elif tag == 'CHANGE_CURRENCY':
                    message = f'{date_text}\nThe currency was changed'
                elif tag == 'GIVE':
                    message = f'{date_text}\nI gave money to somebody'
                elif tag == 'TAKE':
                    message = f'{date_text}\nI took money from somebody'
                else:
                    message = f'{date_text}\nUnknown tag'
                ans.append(message)
            else:
                ans.append(str(transaction))
        return f'\n' + '\n\n'.join(ans)
