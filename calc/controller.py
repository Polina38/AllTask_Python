import User.inputdate as ID
import Base.keepbox as KB
import Operation.oper as OS
import User.outputdate as OD
import Base.logger as BL

def button_click():
    value_a,value_b= ID.InputDate()
    KB.Saver(value_a,value_b)
    x1,y1=KB.Keeper()

    result= OS.Summ(x1,y1)
    BL.calc_logger(x1,y1,result)
    OD.OutputDate(result)


