
def saver_data_txt(data1, data2, data3, data4):
    with open('phonebook.txt', 'a') as file:
        file.write('{};{};{};{}\n'. format(data1, data2, data3, data4))


def saver_data_csv(data1, data2, data3, data4):
    with open('phonebook.csv', 'a') as file:
        file.write('{};{};{};{}\n'. format(data1, data2, data3, data4))
