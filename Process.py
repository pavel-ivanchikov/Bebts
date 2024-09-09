import datetime
from Transaction import Transaction


class Process:
    def __init__(self, identifier: tuple[float, float]):
        self.__data = []
        self._me = identifier[0]
        self._parent = identifier[1]
        self._able = {'INFO': self.info, 'SPLIT': self.split, 'CROSS': self.cross}
        self._reminder = None
        self.related_processes = []

    def add_transaction(self, transaction: Transaction, init: bool):
        if not init:
            # Тут происходит сериализация
            name = r"C:/DebtCounter/first/" + str(int(self._me * 10 ** 6))
            with open(name, 'a', encoding='UTF-8') as file:
                if transaction.official:
                    file.write(str(transaction.date) + ' +\n')
                else:
                    file.write(str(transaction.date) + '\n')
                file.write(transaction.text + '\n')
        self.__data.append(transaction)

    def act(self, text, date=None, official=False):
        if date:
            init = True
        else:
            init = False
            date = datetime.datetime.now(datetime.timezone.utc).timestamp()
        if official:
            tag = text.split(' ')[0]
            if tag in self._able:
                return self._able[tag](text, date, init)
            else:
                raise ValueError('Wrong Tag')
        else:
            self.add_transaction(Transaction(date, text, official), init)

    def info(self, text, date, init):
        pass

    def split(self, text, date, init):
        self.add_transaction(Transaction(date, f'SPLIT {date} from {self._me}', True), init)
        process = Process((date, self._me))
        process.add_transaction(Transaction(date, f'INFO New: {date} from {self._me}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)
        return process

    def cross(self, text, date, init):
        other_id = float(text.split()[1])
        process = self.get_process(other_id)
        self.add_transaction(Transaction(date, f'CROSS {other_id} and {self._me}', True), init)
        process.add_transaction(Transaction(date, f'INFO CROSS {self._me} and {other_id}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)

    def get_process(self, identifier):
        checked_processes = []
        for process in self.related_processes:
            if process not in checked_processes:
                if process.get_identifier()[0] == identifier:
                    return process
                else:
                    checked_processes.append(process)
                    return process.get_process(identifier)
        raise ValueError('No process with such ID')

    def get_identifier(self):
        return self._me, self._parent

    def __repr__(self):
        return f'\nProcess {self.get_identifier()}:' + '\n' + \
                '\n-\n'.join(map(lambda x: str(x), reversed(self.__data)))

    @classmethod
    def create_first_process(cls, date=None):
        init = True
        if date is None:
            date = datetime.datetime.now(datetime.timezone.utc).timestamp()
            init = False
        process = Process((date, 0))
        process.add_transaction(Transaction(date, f'INFO New: {date} from {0}', True), init)
        return process
