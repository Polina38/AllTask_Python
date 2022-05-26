import UI.input_data as ID
import UI.output_data as OD
import Data_Base.logger as DL
import Data_Base.saver as DS
import Data_Base.seacher as BS


def buttom_click():
    change = int(input('Enter number: 1 add new contact, 2 search contact '))
    if change == 1:
        a, b, c, d = ID.my_spisok()
        DS.saver_data_csv(a, b, c, d)
        DS.saver_data_txt(a, b, c, d)
        DL.phonebook_logger(a, b, c, d)

    if change == 2:
        fio = ID.my_spisok_search()
        result = BS.seacher_data(fio)
        OD.printer(result)
