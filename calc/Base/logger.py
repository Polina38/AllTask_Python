
from datetime import datetime as DT
from re import M

def calc_logger(a,b,c):
    with open ('log.csv', 'a') as file:
        time= DT.now().strftime('%D:%H:%M')
        file.write('{} ; {} first count; {} second count; {} summ \n'. format(time,a,b,c))
