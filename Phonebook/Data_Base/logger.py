

from datetime import datetime as DT


def phonebook_logger(data1, data2, data3, data4):
    with open('phonebooklog.csv', 'a') as file:
        time = DT.now().strftime('%D:%H:%M')
        file.write('{} ; last name {}; first name {}; phone number {}; description {}\n'.format(
            time, data1, data2, data3, data4))
