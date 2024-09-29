import datetime
from Transaction import Transaction
from Process import Process
from Person import Person


class MyLife(Process):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.persons = []
        self.additional_ables = {'NEW_PERSON': self.new_person, 'CHANGE_NAME': self.change_name, 'CHANGE_BIRTHDAY': self.change_birthday}
        self._able.update(self.additional_ables)
        self.name = 'Main Process'
        self.birthday = None

    def new_person(self, _, date: float, init: bool):
        self.add_transaction(Transaction(date, f'NEW_PERSON {date} from {self._me}', True), init)
        process = Person((date, self._me))
        process.add_transaction(Transaction(date, f'INFO New person: {date} from {self._me}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)
        self.persons.append(process)
        return process

    def change_name(self, text, date: float, init: bool):
        new_name = text.split(' ')[1]
        self.add_transaction(Transaction(date, f'CHANGE_NAME {new_name} from {self.name}', True), init)
        self.name = new_name

    def change_birthday(self, text, date: float, init: bool):
        new_birthday = text.split(' ')[1]
        self.add_transaction(Transaction(date, f'CHANGE_BIRTHDAY {new_birthday} from {self.birthday}', True), init)
        self.birthday = new_birthday

    def get_all_transaction(self):
        ans = []
        for transaction in reversed(self.get_data()):
            if transaction.official:
                date = datetime.datetime.fromtimestamp(transaction.date)
                date_text = date.strftime("%Y-%m-%d %H:%M:%S")
                tag = transaction.text.split()[0]
                if tag == 'INFO':
                    tag2 = transaction.text.split()[1]
                    if tag2 == 'New:':
                        message = f'{date_text}\nThe process was created'
                    elif tag2 == 'CROSS':
                        message = f'{date_text}\nThe process was crossed'
                    else:
                        message = f'{date_text}\nSome another information'
                elif tag == 'CROSS':
                    message = f'{date_text}\nThe process was crossed'
                elif tag == 'NEW_PERSON':
                    message = f'{date_text}\nNew person was created'
                elif tag == 'CHANGE_NAME':
                    message = f'{date_text}\nThe name of main process was changed'
                elif tag == 'CHANGE_BIRTHDAY':
                    message = f'{date_text}\nThe birth day was changed'
                else:
                    message = f'{date_text}\nUnknown tag'
                ans.append(message)
            else:
                ans.append(str(transaction))
        return f'\n' + '\n\n'.join(ans)
        # return f'\n' + '\n\n'.join(map(lambda x: str(x), reversed(self.__data)))

    @classmethod
    def create_first_process(cls, date=None):
        init = True
        if date is None:
            date = datetime.datetime.now(datetime.timezone.utc).timestamp()
            init = False
        process = MyLife((date, 0))
        process.add_transaction(Transaction(date, f'INFO New: {date} from {0}', True), init)
        return process
