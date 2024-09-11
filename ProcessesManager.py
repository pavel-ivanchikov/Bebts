from Transaction import Transaction
from Process import Process


class ProcessesManager:
    def __init__(self, path: str, first_process_name: str):
        self.path = path
        self.first_process_name = first_process_name
        self.main_dict = {}
        self.temp_message_dict = {}
        first_process = Process.create_first_process(int(first_process_name) / 10 ** 6)
        self.main_dict[first_process_name] = first_process
        self._read(first_process_name) # Тут происходит считывание транзакций всего дерева процессов.
        self._acting()  # Тут происходит десериализация

    def _read(self, name):
        self.temp_message_dict[name] = []
        with open(self.path + name + '.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                date = float(lines[i].split(' ')[0])
                text = lines[i + 1].strip()
                official = False
                if len(lines[i].split(' ')) > 1:
                    official = True
                self.temp_message_dict[name].append(Transaction(date, text, official))
                tag = text.split(' ')[0]
                if official and tag == 'SPLIT':
                    name1 = str(round(float(text.split(' ')[1]) * 10 ** 6))
                    self._read(name1)

    def _acting(self):
        # Тут происходит десериализация
        temp = []
        for name in self.temp_message_dict.keys():
            if len(self.temp_message_dict[name]) > 0:
                temp.append((self.temp_message_dict[name][0].date, name))
        if len(temp) == 0:
            return 0
        next_process_name = min(temp)[1]
        transaction = self.temp_message_dict[next_process_name][0]
        self.temp_message_dict[next_process_name].pop(0)
        tag = transaction.text.split(' ')[0]
        if transaction.official and tag == 'SPLIT':
            process = self.main_dict[next_process_name].act(transaction.text, transaction.date, transaction.official)
            name1 = str(round(float(transaction.text.split(' ')[1]) * 10 ** 6))
            self.main_dict[name1] = process
        else:
            self.main_dict[next_process_name].act(transaction.text, transaction.date, transaction.official)
        self._acting()
