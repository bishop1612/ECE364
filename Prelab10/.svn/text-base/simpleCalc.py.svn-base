# Import PySide classes
import string
import operator
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *


class calc(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(calc, self).__init__(parent)
        self.setupUi(self)
        self.main_output.setText("0.")
        self.expression = ""
        self.setWindowTitle('First Qt Application - Preview')
        self.btn_0.clicked.connect(lambda: self.append(0))
        self.btn_1.clicked.connect(lambda: self.append(1))
        self.btn_2.clicked.connect(lambda: self.append(2))
        self.btn_3.clicked.connect(lambda: self.append(3))
        self.btn_4.clicked.connect(lambda: self.append(4))
        self.btn_5.clicked.connect(lambda: self.append(5))
        self.btn_6.clicked.connect(lambda: self.append(6))
        self.btn_7.clicked.connect(lambda: self.append(7))
        self.btn_8.clicked.connect(lambda: self.append(8))
        self.btn_9.clicked.connect(lambda: self.append(9))

        self.btn_add.clicked.connect(lambda: self.append('+'))
        self.btn_multiply.clicked.connect(lambda: self.append('*'))
        self.btn_sub.clicked.connect(lambda: self.append('-'))
        self.btn_div.clicked.connect(lambda: self.append('/'))
        self.btn_equals.clicked.connect(lambda: self.append('='))
        self.btn_clear.clicked.connect(lambda: self.append('C'))
        self.btn_decimal.clicked.connect(lambda: self.append('.'))


    def append(self,expr):
        if expr == 'C':
            self.main_output.setText("0.")
            self.expression = ""
        elif expr == '=':
            self.expression = str(self.evaluate())
            decimals = self.spinBox_decimals.value()
            if self.expression != "Error in Mathematical Expression. Press C to start over again":
                if self.checkBox_thousands.isChecked() == True:
                    if decimals == 0:
                        new_expr = "{0:,}".format(int(float(self.expression)))
                        self.expression = str(new_expr)
                    else:
                        decimals = "{0:,."+str(decimals)+"f}"
                        print(decimals)
                        self.expression = decimals.format(float(self.expression))
                elif decimals == 0 :
                    new_expr = int(float(self.expression))
                    self.expression = str(new_expr)
                else:
                    decimals = "{0:,."+str(decimals)+"f}"
                    print(decimals)

            new = self.expression.replace(",","")
            if len(new) > 12 and new != "Error in Mathematical Expression. Press C to start over again":
                self.expression = "Output has more than 12 digits. Press C to start over again"
        else:
            self.expression += str(expr)

        if expr != 'C':
            self.main_output.setText(self.expression)

    def evaluate(self):
        operators = set('+-*/')
        op_out = []    #This holds the operators that are found in the string (left to right)
        num_out = []   #this holds the non-operators that are found in the string (left to right)
        buff = []
        number = self.expression.replace(",","")

        for c in number:  #examine 1 character at a time
            if c in operators:
                #found an operator.  Everything we've accumulated in `buff` is
                #a single "number". Join it together and put it in `num_out`.
                num_out.append(''.join(buff))
                buff = []
                op_out.append(c)
            else:
                #not an operator.  Just accumulate this character in buff.
                buff.append(c)
        num_out.append(''.join(buff))

        for num in num_out:
            if num == "":
                return "Error in Mathematical Expression. Press C to start over again"

        return(self.my_eval(num_out,op_out))

    def my_eval(self,nums,ops):
        nums = list(nums)
        ops = list(ops)
        operator_order = ('*/','+-')  #precedence from left to right.  operators at same index have same precendece.
                                      #map operators to functions.
        op_dict = {'*':operator.mul,'/':operator.truediv,'+':operator.add,'-':operator.sub}
        Value = None
        for op in operator_order:                   #Loop over precedence levels
            while any(o in ops for o in op):        #Operator with this precedence level exists
                try:
                    idx,oo = next((i,o) for i,o in enumerate(ops) if o in op) #Next operator with this precedence
                    ops.pop(idx)                        #remove this operator from the operator list
                    values = map(float,nums[idx:idx+2]) #here I just assume float for everything
                    value = op_dict[oo](*values)
                    nums[idx:idx+2] = [value]#clear out those indices
                except ZeroDivisionError:
                    return float('Inf')

        final_num = nums[0]
        return final_num

    def mysplit(self):
        return re.split("([+-/*])", self.expression.replace(" ", ""))


currentApp = QApplication(sys.argv)
currentForm = calc()

currentForm.show()
currentApp.exec_()